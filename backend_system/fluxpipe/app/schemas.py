from datetime import datetime
from pydantic import BaseModel, Field


class JobCreate(BaseModel):
    type: str = Field(..., examples=["clean_csv", "sort_files"])
    input_path: str | None = None


class JobOut(BaseModel):
    id: str
    type: str
    status: str
    input_path: str | None
    output_path: str | None
    error: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class JobStatusUpdate(BaseModel):
    status: str = Field(..., examples=["pending", "running", "completed", "failed"])
    output_path: str | None = None
    error: str | None = None
