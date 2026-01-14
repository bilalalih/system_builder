from fastapi import FastAPI
from .db import engine, Base
from .api import router

def create_app() -> FastAPI:
    app = FastAPI(title="FluxPipe (Phase 1)")
    app.include_router(router)
    return app

# Create tables on startup (fine for Phase 1)
Base.metadata.create_all(bind=engine)

app = create_app()
