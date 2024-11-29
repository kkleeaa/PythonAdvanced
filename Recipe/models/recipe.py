from pydantic import BaseModel

from typing import Optional





class RecipeBase(BaseModel):

    name: str

    description: Optional[str]

    ingridients: str

    instructions: str

    cuisine: str

    difficulty: str

    category_id: Optional[str]





class RecipeCreate(RecipeBase):

    pass





class Recipe(RecipeBase):

    id: int
    