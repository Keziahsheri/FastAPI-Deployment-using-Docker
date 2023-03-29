from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    
class Role(str, Enum):
    user = 'user'
    admin ='admin'
  
class User(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name : str
    last_name :str
    middle_name : Optional[str]
    gender : Gender
    roles: Role

    class Config:
        orm_mode = True