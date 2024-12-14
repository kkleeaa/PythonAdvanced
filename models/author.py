from pydantic import BaseModel

class AuthorBase(BaseModel):
    name:str
class AuthorCreate(AuthorBase):
    pass
class AuthorResponse(BaseModel):
    id:int
    name:str
class Author(AuthorBase):
    id:int