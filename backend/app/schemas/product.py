from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(
        ..., min_length=5, max_length=200, description="Name of the product"
    )
    description: Optional[str] = Field(
        None, min_length=10, max_length=1000, description="Description of the product"
    )
    price: float = Field(..., gt=0, description="Price of the product")

    category: int = Field(..., description="ID of the category")
    image_url: Optional[str] = Field(None, description="URL of the product image")


class ProductCreate(ProductBase):
    pass


class ProductResponse(BaseModel):
    id: int = Field(..., description="ID of the product")
    name: str
    description: Optional[str]
    price: float
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description="Category of the product")

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")

    class Config:
        from_attributes = True
