
from typing import List
from fastapi import Depends, status, APIRouter
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import puppy_crud

router = APIRouter(
    prefix="/shop",
    tags = ['puppies']
)

@router.get('/', response_model=List[schemas.ShowPuppy])
def all(db : Session = Depends(get_db)):
    return puppy_crud.read_all(db)

@router.get('/{id}', status_code=200)
def getPup(id, db : Session = Depends(get_db)):
    return puppy_crud.read_one(db, id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowPuppy)
def create(request: schemas.Puppy, db : Session = Depends(get_db)):
    return puppy_crud.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Puppy, db : Session = Depends(get_db)):
    return puppy_crud.update(id, request, db)

@router.delete('/{id}')
def delete(id, db: Session = Depends(get_db)):
    return puppy_crud.delete(id, db)