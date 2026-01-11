from sort_file import sort_files
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OrganiseRequest(BaseModel):
    path: str

@app.post("/path/sort_file_backend")
def sort_file_backend(request: OrganiseRequest):
    sort_files(request.path)
    return {"staus": "completed", "path": request.path}