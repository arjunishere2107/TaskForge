from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.routes import auth, projects, tasks
from app.models import user, project, task

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication Routes
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

# Project Routes
app.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"]
)

# Task Routes
app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)

@app.get("/")
def home():
    return {
        "message": "TaskForge API Running"
    }