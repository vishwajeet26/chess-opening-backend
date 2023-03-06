from .. import database, models
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['Openings'], prefix='/opening')

get_db = database.get_db

@router.post('/')
def create(request: schemas.Opening,db: Session = Depends(get_db)):
    new_opening = models.Opening(moves=request.moves, name=request.name, ecocode=request.ecocode, description=request.description)
    db.add(new_opening)
    db.commit()
    db.refresh(new_opening)
    return f'Opening - {request.name} has been posted.'

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    opening = db.query(models.Opening).all()
    return opening

@router.get('/{ecocode}}')
def get(ecocode: str, db: Session = Depends(get_db)):
    opening = db.query(models.Opening).filter(models.Opening.ecocode == ecocode).first()
    if not opening: 
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Opening with the Eco code - {ecocode} does not exist.")
    return opening

@router.delete('/{ecocode}')
def destroy(ecocode: str, db: Session = Depends(get_db)):
    opening = db.query(models.Opening).filter(models.Opening.ecocode == ecocode)
    if not opening.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Opening with id {id} is not found")
    opening.delete(synchronize_session=False)
    db.commit()
    return f'The opening with ecocode-{ecocode} was deleted.'

@router.put('/{id}', status_code=202)
def update(id: int, request: schemas.Opening, db: Session = Depends(get_db)):
    opening = db.query(models.Opening).filter(models.Opening.id == id)
    if not opening.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Opening with id {id} is not found")
    opening.update({'name': request.name, 'description': request.description})
    db.commit()
    return 'updated'
