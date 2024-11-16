from pydantic import BaseModel
from typing import List, Optional
class Developer(BaseModel):
    name:str
    experience:Optional[int]=None
class Project(BaseModel):
    title:str
    description: Optional[str]=None
    languages:Optional[List[str]]=[]
    lead_developer:Developer

    