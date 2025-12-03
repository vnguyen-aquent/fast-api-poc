from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    full_name: str
    is_active: bool = True


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime


class UserUpdate(SQLModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None