package main

import (
	"context"
	"fmt"
	"math/rand"
	"os"
	"os/signal"
	"syscall"
	"time"

	"job-queue/queue"
)

func main() {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Graceful shutdown on Ctrl+C
	sigCh := make(chan os.Signal, 1)
	signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)
	go func() {
		<-sigCh
		fmt.Println("\n[shutdown] signal received, stopping intake...")
		cancel()
	}()

	q := queue.New(100)

	workers := 4
	q.StartWorkers(ctx, workers)

	// Enqueue 50 demo jobs
	for i := 1; i <= 50; i++ {
		id := fmt.Sprintf("job-%03d", i)

		err := q.Enqueue(queue.Job{
			ID:         id,
			MaxRetries: 3,
			Run: func(ctx context.Context) error {
				// simulate variable work time
				time.Sleep(time.Duration(50+rand.Intn(150)) * time.Millisecond)

				// simulate failures ~25% of the time
				if r.Intn(4) == 0 {
					return fmt.Errorf("random failure")
				}
				return nil
			},
		})
		if err != nil {
			fmt.Printf("[enqueue] %s: %v\n", id, err)
		}
	}

	// Stop intake after enqueueing is done
	q.StopIntake()

	// Wait for all work to complete
	q.Wait()

	s := q.Stats()
	fmt.Println("\n=== STATS ===")
	fmt.Printf("Enqueued:  %d\n", s.Enqueued)
	fmt.Printf("Started:   %d\n", s.Started)
	fmt.Printf("Succeeded: %d\n", s.Succeeded)
	fmt.Printf("Retried:   %d\n", s.Retried)
	fmt.Printf("Failed:    %d\n", s.Failed)
}
