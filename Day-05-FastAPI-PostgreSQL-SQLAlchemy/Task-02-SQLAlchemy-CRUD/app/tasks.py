from collections import defaultdict
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .database import get_db
from .dependencies import get_current_user, require_teacher
from .models import Task, User
from .schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/api/v3", tags=["Tasks"])


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    payload: TaskCreate,
    teacher: Annotated[User, Depends(require_teacher)],
    db: Annotated[Session, Depends(get_db)],
) -> Task:
    if payload.assigned_to is not None:
        _get_student(db, payload.assigned_to)
    task = Task(
        title=payload.title,
        description=payload.description,
        assigned_to=payload.assigned_to,
        assigned_by=teacher.id,
        status="pending",
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
) -> list[Task]:
    statement = select(Task).order_by(Task.id)
    if user.role == "student":
        statement = statement.where(Task.assigned_to == user.id)
    return list(db.scalars(statement).all())


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: int,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
) -> Task:
    task = _get_task(db, task_id)
    if user.role == "student" and task.assigned_to != user.id:
        raise _task_not_found()
    return task


@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
) -> Task:
    task = _get_task(db, task_id)
    changes = payload.model_dump(exclude_unset=True)

    if user.role == "student":
        if task.assigned_to != user.id:
            raise _task_not_found()
        if changes.keys() - {"status", "work_notes"}:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Students may only update task status and work notes.",
            )
    elif user.role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher or student role is required.",
        )

    if any(
        field in changes and changes[field] is None
        for field in ("title", "status")
    ):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Task title and status cannot be null.",
        )
    if changes.get("assigned_to") is not None:
        _get_student(db, changes["assigned_to"])

    for field, value in changes.items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    _: Annotated[User, Depends(require_teacher)],
    db: Annotated[Session, Depends(get_db)],
) -> None:
    task = _get_task(db, task_id)
    db.delete(task)
    db.commit()


@router.get("/progress")
def read_progress(
    _: Annotated[User, Depends(require_teacher)],
    db: Annotated[Session, Depends(get_db)],
) -> dict[str, object]:
    students = list(
        db.scalars(select(User).where(User.role == "student").order_by(User.id)).all()
    )
    counts = db.execute(
        select(Task.assigned_to, Task.status, func.count(Task.id))
        .where(Task.assigned_to.is_not(None))
        .group_by(Task.assigned_to, Task.status)
    ).all()
    progress: dict[int, dict[str, int]] = defaultdict(
        lambda: {"pending": 0, "in progress": 0, "done": 0}
    )
    for student_id, task_status, count in counts:
        progress[student_id][task_status] = count

    return {
        "students": [
            {
                "user_id": student.id,
                "name": student.name,
                "pending": progress[student.id]["pending"],
                "in_progress": progress[student.id]["in progress"],
                "done": progress[student.id]["done"],
            }
            for student in students
        ]
    }


def _get_student(db: Session, user_id: int) -> User:
    student = db.get(User, user_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found.",
        )
    if student.role != "student":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Tasks can only be assigned to students.",
        )
    return student


def _get_task(db: Session, task_id: int) -> Task:
    task = db.get(Task, task_id)
    if task is None:
        raise _task_not_found()
    return task


def _task_not_found() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found.",
    )
