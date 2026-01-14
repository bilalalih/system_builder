from sqlalchemy.orm import Session
from .models import Job
from datetime import datetime, timezone


def create_job(db: Session, job: Job) -> Job:
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_job(db: Session, job_id: str) -> Job | None:
    return db.get(Job, job_id)


def update_job_status(
    db: Session,
    job: Job,
    *,
    status: str,
    output_path: str | None = None,
    error: str | None = None,
) -> Job:
    job.status = status
    if output_path is not None:
        job.output_path = output_path
    if error is not None:
        job.error = error
    job.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(job)
    return job
