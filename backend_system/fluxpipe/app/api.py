import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .deps import get_db
from .models import Job, JobStatus
from .schemas import JobCreate, JobOut, JobStatusUpdate
from .crud import create_job, get_job, update_job_status

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/jobs", response_model=JobOut)
def create_job_endpoint(payload: JobCreate, db: Session = Depends(get_db)):
    job = Job(
        id=str(uuid.uuid4()),
        type=payload.type,
        status=JobStatus.pending.value,
        input_path=payload.input_path,
    )
    return create_job(db, job)


@router.get("/jobs/{job_id}", response_model=JobOut)
def get_job_endpoint(job_id: str, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.patch("/jobs/{job_id}", response_model=JobOut)
def update_job_endpoint(job_id: str, payload: JobStatusUpdate, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return update_job_status(
        db,
        job,
        status=payload.status,
        output_path=payload.output_path,
        error=payload.error,
    )
