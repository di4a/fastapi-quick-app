from typing import List
from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from .. import schemas
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from ..repository import user_crud


router = APIRouter(
    prefix="/blog",
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_crud.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user_crud.read_one(id, db)