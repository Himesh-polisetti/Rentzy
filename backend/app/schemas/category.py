"""Category schemas"""
from pydantic import BaseModel


class CategoryResponse(BaseModel):
    """Category response schema"""
    id: str
    name: str
    description: str
    icon: str

    class Config:
        """Config"""
        from_attributes = True