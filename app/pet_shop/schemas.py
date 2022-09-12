from typing import List, Optional
from pydantic import BaseModel

class Puppy(BaseModel):
    name : str
    breed : Optional[str]
    age : int
    class Config():
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    #puppies : List[Puppy] = []
    #this dont belong here
    class Config():
        orm_mode = True

class ShowPuppy(BaseModel):
    name : str
    owner : ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str


