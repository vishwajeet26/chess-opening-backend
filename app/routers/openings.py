from .. import database, models
from fastapi import APIRouter, Depends
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
