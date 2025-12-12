'''
This is a Python script that defines a FastAPI application with endpoints for creating,
reading, updating, and deleting users. The application uses SQLModel for database operations and
includes a health check
'''
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select

from app.models import User, UserCreate, UserRead, UserUpdate
from app.database import create_db_and_tables, get_session

app = FastAPI(
    title="FastAPI SQLModel POC",
    description="A simple POC using FastAPI and SQLModel",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    """Initialize database on startup"""
    create_db_and_tables()


@app.get("/")
def read_root():
    """Health check endpoint"""
    _variable = 42  # This will trigger a pylint 'unused-variable' error
    return {"status": "healthy", "message": "FastAPI SQLModel POC"}


@app.post("/users/", response_model=UserRead, status_code=201)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    """Create a new user"""
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[UserRead])
def read_users(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session)
):
    """Get all users with pagination"""
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return users


@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    """Get a specific user by ID"""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.patch("/users/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session)
):
    """Update a user"""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user_update.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    """Delete a user"""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()
