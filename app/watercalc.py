from . import models, database
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional

                 
class WaterStats:
    def __init__(self, 
                 station_id: int, 
                 station_code: str, 
                 min_water_level_observed_date_alltime: datetime,
                 min_water_level_alltime: float,
                 min_water_level_units_alltime: str,
                 max_water_level_observed_date_alltime: datetime,
                 max_water_level_alltime: float,
                 max_water_level_units_alltime: str,
                 min_water_flow_observed_date_alltime: datetime,
                 min_water_flow_alltime: float,
                 min_water_flow_units_alltime: str,
                 max_water_flow_observed_date_alltime: datetime,
                 max_water_flow_alltime: float,
                 max_water_flow_units_alltime: str,
                 current_water_level_observed_date: datetime,
                 current_water_level: float,
                 current_water_level_units: str,
                 current_water_flow: float,
                 current_water_flow_units: str,
                 min_water_level_observed_date_10day: datetime,
                 min_water_level_10day: float,
                 min_water_level_units_10day: str,
                 max_water_level_observed_date_10day: datetime,
                 max_water_level_10day: float,
                 max_water_level_units_10day: str,
                 min_water_flow_observed_date_10day: datetime,
                 min_water_flow_10day: float,
                 min_water_flow_units_10day: str,
                 max_water_flow_observed_date_10day: datetime,
                 max_water_flow_10day: float,
                 max_water_flow_units_10day: str):

        self.station_id = station_id
        self.station_code = station_code
        self.min_water_level_observed_date_alltime = min_water_level_observed_date_alltime
        self.min_water_level_alltime = min_water_level_alltime
        self.min_water_level_units_alltime = min_water_level_units_alltime
        self.max_water_level_observed_date_alltime = max_water_level_observed_date_alltime
        self.max_water_level_alltime = max_water_level_alltime
        self.max_water_level_units_alltime = max_water_level_units_alltime
        self.min_water_flow_observed_date_alltime = min_water_flow_observed_date_alltime
        self.min_water_flow_alltime = min_water_flow_alltime
        self.min_water_flow_units_alltime = min_water_flow_units_alltime
        self.max_water_flow_observed_date_alltime = max_water_flow_observed_date_alltime
        self.max_water_flow_alltime = max_water_flow_alltime
        self.max_water_flow_units_alltime = max_water_flow_units_alltime
        self.current_water_level_observed_date = current_water_level_observed_date
        self.current_water_level = current_water_level
        self.current_water_level_units = current_water_level_units
        self.current_water_flow = current_water_flow
        self.current_water_flow_units = current_water_flow_units
        self.min_water_level_observed_date_10day = min_water_level_observed_date_10day
        self.min_water_level_10day = min_water_level_10day
        self.min_water_level_units_10day = min_water_level_units_10day
        self.max_water_level_observed_date_10day = max_water_level_observed_date_10day
        self.max_water_level_10day = max_water_level_10day
        self.max_water_level_units_10day = max_water_level_units_10day
        self.min_water_flow_observed_date_10day = min_water_flow_observed_date_10day
        self.min_water_flow_10day = min_water_flow_10day
        self.min_water_flow_units_10day = min_water_flow_units_10day
        self.max_water_flow_observed_date_10day = max_water_flow_observed_date_10day
        self.max_water_flow_10day = max_water_flow_10day
        self.max_water_flow_units_10day = max_water_flow_units_10day
       # self. = 
        # self. = 
        # self. = 

    def __repr__(self):
        return f"{self.__class__.__name__}({self.station_id}, \
        '{self.station_code}', \
        {self.min_water_level_observed_date_alltime},\
        {self.min_water_level_alltime},\
        {self.min_water_level_units_alltime},\
        {self.max_water_level_observed_date_alltime},\
        {self.max_water_level_alltime},\
        {self.max_water_level_units_alltime},\
        {self.min_water_flow_observed_date_alltime},\
        {self.min_water_flow_alltime},\
        {self.min_water_flow_units_alltime},\
        {self.max_water_flow_observed_date_alltime},\
        {self.max_water_flow_alltime},\
        {self.max_water_flow_units_alltime},\
        {self.current_water_level_observed_date},\
        {self.current_water_level},\
        {self.current_water_level_units},\
        {self.current_water_flow},\
        {self.current_water_flow_units},\
        {self.min_water_level_observed_date_10day},\
        {self.min_water_level_10day},\
        {self.min_water_level_units_10day},\
        {self.max_water_level_observed_date_10day},\
        {self.max_water_level_10day},\
        {self.max_water_level_units_10day}"


def GetWaterReport(station_code: str, db: Session):

    WaterCurrent = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code).order_by(models.WaterReport.published_date.desc()).limit(1).first()
    # print(f'====Current:{WaterCurrent}')

    WaterMinLevelAllTime = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code).order_by(models.WaterReport.water_level).limit(1).first()
    # print(f'====MinLevelAllTime:{WaterMinLevelAllTime}')

    WaterMinLevel10Day = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code, models.WaterReport.observed_date > datetime.now() - timedelta(days=10)).order_by(models.WaterReport.water_level).limit(1).first()
    # print(f'====MinLevelAllTime:{WaterMinLevel10Day}')

    WaterMinFlowAllTime = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code).order_by(models.WaterReport.water_flow).limit(1).first()
    # print(f'====MinFlowAllTime:{WaterMinFlowAllTime}')

    WaterMinFlow10Day = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code, models.WaterReport.observed_date > datetime.now() - timedelta(days=10)).order_by(models.WaterReport.water_flow).limit(1).first()
    # print(f'====MinLevelAllTime:{WaterMinFlow10Day}')

    WaterMaxLevelAllTime = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code).order_by(models.WaterReport.water_level.desc()).limit(1).first()
    # print(f'====MinFlowAllTime:{WaterMaxLevelAllTime}')

    WaterMaxLevel10Day = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code, models.WaterReport.observed_date > datetime.now() - timedelta(days=10)).order_by(models.WaterReport.water_level.desc()).limit(1).first()
    # print(f'====MinLevelAllTime:{WaterMaxLevel10Day}')

    WaterMaxFlow10Day = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code, models.WaterReport.observed_date > datetime.now() - timedelta(days=10)).order_by(models.WaterReport.water_flow.desc()).limit(1).first()
    # print(f'====MinLevelAllTime:{WaterMaxFlow10Day}')

    WaterMaxFlowAllTime = db.query(models.WaterReport).filter(
    models.WaterReport.station_code == station_code).order_by(models.WaterReport.water_flow.desc()).limit(1).first()
    # print(f'====MinFlowAllTime:{WaterMaxFlowAllTime}')



    waterstats = WaterStats(WaterCurrent.station_id, 
                            WaterCurrent.station_code, 
                            WaterMinLevelAllTime.observed_date, 
                            WaterMinLevelAllTime.water_level, 
                            WaterMinLevelAllTime.water_level_units, 
                            WaterMaxLevelAllTime.observed_date, 
                            WaterMaxLevelAllTime.water_level, 
                            WaterMaxLevelAllTime.water_level_units, 
                            WaterMinFlowAllTime.observed_date, 
                            WaterMinFlowAllTime.water_flow, 
                            WaterMinFlowAllTime.water_flow_units, 
                            WaterMaxFlowAllTime.observed_date, 
                            WaterMaxFlowAllTime.water_flow, 
                            WaterMaxFlowAllTime.water_flow_units, 
                            WaterCurrent.observed_date, 
                            WaterCurrent.water_level, 
                            WaterCurrent.water_level_units, 
                            WaterCurrent.water_flow, 
                            WaterCurrent.water_flow_units,
                            WaterMinLevel10Day.observed_date,
                            WaterMinLevel10Day.water_level,
                            WaterMinLevel10Day.water_level_units,
                            WaterMaxLevel10Day.observed_date,
                            WaterMaxLevel10Day.water_level,
                            WaterMaxLevel10Day.water_level_units,
                            WaterMinFlow10Day.observed_date,
                            WaterMinFlow10Day.water_flow,
                            WaterMinFlow10Day.water_flow_units,
                            WaterMaxFlow10Day.observed_date,
                            WaterMaxFlow10Day.water_flow,
                            WaterMaxFlow10Day.water_flow_units)
    
    # print(waterstats)
    return waterstats