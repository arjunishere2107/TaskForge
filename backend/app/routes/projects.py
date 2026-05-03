from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can create projects"
        )

    new_project = Project(
        name=project.name,
        description=project.description,
        created_by=current_user["id"]
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project": new_project
    }

@router.get("/")
def get_projects(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    projects = db.query(Project).all()

    return projects