from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
    slug: str


class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    created_at: datetime

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = False
    category_id: Optional[int] = None


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    category_id: Optional[int] = None


class PostResponse(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    published: bool
    author_id: int
    category_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True
