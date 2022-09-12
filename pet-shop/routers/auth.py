from typing import List
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
import schemas
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from hashing import Hash
from repository import user_crud

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request:schemas.Login, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
         detail=f'User {request.username} does not exist')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
         detail= 'Incorrect password')

    return user