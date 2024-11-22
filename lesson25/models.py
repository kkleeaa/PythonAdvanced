from pydantic import BaseModel

class MovieCreate(BaseModel):
    title:str
    director:str

class Movie(MovieCreate):
    id:int

