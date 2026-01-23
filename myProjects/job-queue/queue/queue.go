package queue

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

type JobFunc func(ctx context.Context) error

type Job struct {
	ID         string
	Attempts   int
	MaxRetries int
	Run        JobFunc
}

type Stats struct {
	Enqueued  int64
	Started   int64
	Succeeded int64
	Failed    int64
	Retried   int64
}

type Queue struct {
	jobs    chan Job
	wg      sync.WaitGroup
	stopped atomic.Bool
	stats   Stats
}

func New(buffer int) *Queue {
	return &Queue{
		jobs: make(chan Job, buffer),
	}
}

func (q *Queue) Stats() Stats {
	return Stats{
		Enqueued:  atomic.LoadInt64(&q.stats.Enqueued),
		Started:   atomic.LoadInt64(&q.stats.Started),
		Succeeded: atomic.LoadInt64(&q.stats.Succeeded),
		Failed:    atomic.LoadInt64(&q.stats.Failed),
		Retried:   atomic.LoadInt64(&q.stats.Retried),
	}
}

// Enqueue adds a job. Returns error if queue is stopping/stopped.
func (q *Queue) Enqueue(job Job) error {
	if q.stopped.Load() {
		return errors.New("queue is stopping; cannot enqueue")
	}
	atomic.AddInt64(&q.stats.Enqueued, 1)
	q.wg.Add(1)
	q.jobs <- job
	return nil
}

// StartWorkers spins up n worker goroutines.
func (q *Queue) StartWorkers(ctx context.Context, n int) {
	for i := 0; i < n; i++ {
		workerID := i + 1
		go q.workerLoop(ctx, workerID)
	}
}

// StopIntake closes the jobs channel so no more jobs can be enqueued.
// Workers will drain remaining jobs.
func (q *Queue) StopIntake() {
	if q.stopped.CompareAndSwap(false, true) {
		close(q.jobs)
	}
}

// Wait blocks until all enqueued jobs have completed (success or final failure).
func (q *Queue) Wait() {
	q.wg.Wait()
}

func (q *Queue) workerLoop(ctx context.Context, workerID int) {
	for job := range q.jobs {
		atomic.AddInt64(&q.stats.Started, 1)

		err := job.Run(ctx)
		if err == nil {
			atomic.AddInt64(&q.stats.Succeeded, 1)
			q.wg.Done()
			continue
		}

		// Retry logic
		job.Attempts++
		if job.Attempts <= job.MaxRetries {
			atomic.AddInt64(&q.stats.Retried, 1)

			// simple backoff: 100ms * attempts
			backoff := time.Duration(100*job.Attempts) * time.Millisecond
			select {
			case <-time.After(backoff):
			case <-ctx.Done():
				atomic.AddInt64(&q.stats.Failed, 1)
				q.wg.Done()
				continue
			}

			// Re-enqueue only if still accepting jobs
			if q.stopped.Load() {
				atomic.AddInt64(&q.stats.Failed, 1)
				q.wg.Done()
				continue
			}

			// IMPORTANT: do NOT q.wg.Add(1) again (same job lifecycle)
			q.jobs <- job
			continue
		}

		atomic.AddInt64(&q.stats.Failed, 1)
		_ = fmt.Errorf("worker %d: job %s failed after %d attempts: %w", workerID, job.ID, job.Attempts, err)
		q.wg.Done()
	}
}
