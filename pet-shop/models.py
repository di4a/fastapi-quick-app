from code import interact
from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship 

class Puppy(Base):
    __tablename__ = 'puppies'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="puppies")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    puppies = relationship("Puppy", back_populates="owner")