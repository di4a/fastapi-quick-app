from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

def create(request: schemas.Puppy, db : Session):
    new_puppy = models.Puppy(name = request.name, breed = request.breed, age = request.age, owner_id = 1)
    db.add(new_puppy)
    db.commit()
    db.refresh(new_puppy)
    return new_puppy

def read_all(db : Session):
    return db.query(models.Puppy).all()

def read_one(db : Session, id : str):
    pup = db.query(models.Puppy).filter(models.Puppy.id == id).first()
    if not pup:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pup with the id {id} does not exist')
    return pup

def update(id, request: schemas.Puppy, db : Session):
    pup = db.query(models.Puppy).filter(models.Puppy.id == id)
    if not pup.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pup with ID {id} not found')
    pup.update({models.Puppy.name: request.name, models.Puppy.breed : request.breed, models.Puppy.age : request.age})
    db.commit()
    return 'updated'

def delete(id, db: Session):
    db.query(models.Puppy).filter(models.Puppy.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

