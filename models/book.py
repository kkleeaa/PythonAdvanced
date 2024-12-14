from pydantic import BaseModel
from typing import List, Optional
class

class BookBase(BaseModel):
    title:str
    author_id:int
    book_link: str
    genres:List[str]
    average_rating: Optional[float]=None
    published_year= Optional[int]=None
class BookCreate(BookBase):
    pass
class BookResponse(BookBase):
    id:int
class Book(BookBase):
    id:int
