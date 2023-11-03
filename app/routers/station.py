from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from ..import models, schemas, oauth2
from ..database import get_db
from sqlalchemy import func


router = APIRouter(
    prefix="/stations",
    tags=['Stations']
)

# @router.get("/")
@router.get("/",  response_model=List[schemas.StationOutList], response_model_exclude_none=True)
def get_Station(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    stations = db.query(models.Station).filter(
        models.Station.station_description.contains(search)).order_by(models.Station.id).limit(limit).offset(skip).all()

    return stations

@router.get("/{station_code}", response_model=schemas.StationOut)
def get_Station(station_code: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    station = db.query(models.Station).filter(models.Station.station_code == station_code).first()

    if not station:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Station with code: {station_code} does not exist")


    return station