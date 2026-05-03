from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.models.project import Project

from app.schemas.task_schema import TaskCreate, TaskUpdate

from app.utils.dependencies import get_current_user

router = APIRouter()

# CREATE TASK
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can create tasks"
        )

    project = db.query(Project).filter(
        Project.id == task.project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        project_id=task.project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }

# GET TASKS
@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    # admin sees all tasks
    if current_user["role"] == "admin":
        tasks = db.query(Task).all()

    # member sees only assigned tasks
    else:
        tasks = db.query(Task).filter(
            Task.assigned_to == current_user["id"]
        ).all()

    return tasks

# UPDATE TASK STATUS
@router.put("/{task_id}")
def update_task_status(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # member can update only own task
    if (
        current_user["role"] == "member"
        and task.assigned_to != current_user["id"]
    ):
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    task.status = updated_task.status

    db.commit()
    db.refresh(task)

    return {
        "message": "Task updated successfully",
        "task": task
    }