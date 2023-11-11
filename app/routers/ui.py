from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from ..import models, schemas, oauth2, utilities
from ..database import get_db
from sqlalchemy import func
from ..watercalc import GetWaterReport

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

UiRouter = APIRouter(
    prefix="/ui",
    tags=['UI']
)


@UiRouter.get("/")
def get_ui(request: Request, db: Session = Depends(get_db)):

    stations = db.query(models.Station).order_by(models.Station.id).all()

    return templates.TemplateResponse("base.html",
                                      {"request": request, "station_list": stations })


UiSubmitRouter = APIRouter(
    prefix="/uisubmit",
    tags=['UI']
)

@UiRouter.get("/{scode}")
def get_ui(request: Request, scode: str, db: Session = Depends(get_db)):

    WaterStats = GetWaterReport(scode, db)

    stations = db.query(models.Station).order_by(models.Station.id).all()

    return templates.TemplateResponse("WaterStats.html",
                                      {"request": request, "water_stats": WaterStats, "station_list": stations })


UiSubmitRouter = APIRouter(
    prefix="/uisubmit",
    tags=['UI']
)

@UiSubmitRouter.post('')
def submit(request: Request, list_station: str = Form(...)):

    print(f'------{list_station}')

    url = UiRouter.url_path_for("get_ui") + list_station

    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
