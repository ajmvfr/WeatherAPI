from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from ..import models, schemas, oauth2, utilities
from ..database import get_db
from sqlalchemy import func



WaterLevelRouter = APIRouter(
    prefix="/WaterLevels",
    tags=['WaterLevel']
)

@WaterLevelRouter.get("/{station_code}",  response_model=List[schemas.WaterLevel], response_model_exclude_none=True)
def get_WaterLevels(station_code: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0):

    WaterLevel = db.query(models.WaterReport).filter(
        models.WaterReport.station_code == station_code).order_by(models.WaterReport.published_date.desc()).limit(limit).offset(skip).all()


    if not WaterLevel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"water readings with station code: {station_code} does not exist")

    return WaterLevel


WaterReport = APIRouter(
    prefix="/WaterReport",
    tags=['WaterLevel']
)

# @WaterReport.get("/{station_code}")
@WaterReport.get("/{station_code}",  response_model=schemas.WaterReport, response_model_exclude_none=True)
def get_WaterReport(station_code: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    waterreport1 = models.WaterReport


    WaterReport_qry = db.query(waterreport1.station_code,
                               waterreport1.station_id,
                               func.min(waterreport1.observed_date).label('min_observed_date'),
                               func.max(waterreport1.observed_date).label('max_observed_date'),
                               func.min(waterreport1.water_level).label('min_water_level'),
                               func.max(waterreport1.water_level).label('max_water_level'), 
                               func.min(waterreport1.water_flow).label('min_water_flow'),
                               func.max(waterreport1.water_flow).label('max_water_flow'),  
                               ).filter(
        waterreport1.station_code == station_code).group_by(waterreport1.station_code, waterreport1.station_id)

    WaterReport = WaterReport_qry.first()

    if not WaterReport:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"water readings with station code: {station_code} does not exist")

    WaterReportDict = utilities.convert_list_to_model(WaterReport_qry)

    return WaterReportDict  #WaterReport


CurrentWaterReading = APIRouter(
    prefix="/CurrentWaterReading",
    tags=['WaterLevel']
)

@CurrentWaterReading.get("/{station_code}",  response_model=schemas.WaterLevel, response_model_exclude_none=True)
def get_CurrentReading(station_code: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    WaterLevel = db.query(models.WaterReport).filter(
        models.WaterReport.station_code == station_code).order_by(models.WaterReport.published_date.desc()).limit(1).first()
    # WaterLevel = db.query(models.WaterReport).filter(
    #     models.WaterReport.id == 1).order_by(models.WaterReport.published_date.desc()).all()

    if not WaterLevel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"water readings with station code: {station_code} does not exist")
    
    return WaterLevel