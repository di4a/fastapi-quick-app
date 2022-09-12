from typing import List
from fastapi import Depends, FastAPI, status, HTTPException
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from hashing import Hash
from routers import puppy, user, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(puppy.router)
app.include_router(user.router)
app.include_router(auth.router)

# @app.post('/shop', status_code=status.HTTP_201_CREATED, tags=["puppies"])
# def create(request: schemas.Puppy, db : Session = Depends(get_db)):
#     new_puppy = models.Puppy(name = request.name, breed = request.breed, age = request.age, owner_id = 1)
#     db.add(new_puppy)
#     db.commit()
#     db.refresh(new_puppy)
#     return new_puppy

# @app.get('/shop', response_model=List[schemas.ShowPuppy], tags=["puppies"])
# def all(db : Session = Depends(get_db)):
#     pups = db.query(models.Puppy).all()
#     return pups

# @app.delete('/shop/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["puppies"])
# def delete(id, db: Session = Depends(get_db)):
#     db.query(models.Puppy).filter(models.Puppy.id == id).delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/shop/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["puppies"])
# def update(id, request: schemas.Puppy, db : Session = Depends(get_db)):
#     pup = db.query(models.Puppy).filter(models.Puppy.id == id)
#     if not pup.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pup with ID {id} not found')
#     pup.update({request})
#     db.commit()
#     return 'updated'

# @app.get('/shop/{id}', status_code=200, tags=["puppies"])
# def getPup(id, db : Session = Depends(get_db)):
#     pup = db.query(models.Puppy).filter(models.Puppy.id == id).first()
#     if not pup:
#         #exception with HTTPException provided by Fast
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pup with the id {id} does not exist')
        
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {'detail':f'[Pup] with the id {id} does not exist'}
#     return pup

#==============================================

# @app.post('/user', response_model=schemas.ShowUser, tags=["users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=["users"])
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} not found')
#     return user