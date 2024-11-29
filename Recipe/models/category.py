from pydantic import BaseModel





class CategoryBase(BaseModel):

    name: str





class CategoryCreate(CategoryBase):

    pass





class CategoryResponse(BaseModel):

    id: int

    name: str





class Category(CategoryResponse):

    pass

