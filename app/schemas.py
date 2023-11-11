from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class StationOutList(BaseModel):
    station_code: str
    station_description: str
    station_no: Optional[int]
    id: int

    class Config:
        from_attributes = True

class StationOut(BaseModel):
    station_code: str
    station_description: str
    station_no: Optional[int]
    ActionLevel: Optional[float]
    ActionLevelUnits: Optional[str]
    MinorLevel: Optional[float]
    MinorLevelUnits: Optional[str]
    ModerateLevel: Optional[float]
    ModerateLevelUnits: Optional[str]
    MajorLevel: Optional[float]
    MajorLevelUnits: Optional[str]
    ActionFlow: Optional[float]
    ActionFlowUnits: Optional[str]
    MinorFlow: Optional[float]
    MinorFlowUnits: Optional[str]
    ModerateFlow: Optional[float]
    ModerateFlowUnits: Optional[str]
    MajorFlow: Optional[float]
    MajorFlowUnits: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    id: int

    class Config:
        from_attributes = True

class WaterLevel(BaseModel):
    station_id: int
    station_code: str
    published_date: datetime
    observed_date: datetime
    water_category: Optional[str]
    water_level: Optional[float]
    water_level_units: Optional[str]
    water_flow: Optional[float]
    water_flow_units: Optional[str]
    created_at: datetime


    class Config:
        from_attributes = True    


class WaterReport(BaseModel):
    station_id: int
    station_code: str
    min_observed_date: datetime
    max_observed_date: datetime
    min_water_level: Optional[float]
    max_water_level: Optional[float]
    min_water_flow: Optional[float]
    max_water_flow: Optional[float]

    class Config:
        from_attributes = True

class WaterStats(BaseModel):
    station_code: str
    min_water_level_observed_date_alltime: datetime
    min_water_level_alltime: Optional[float]
    min_water_level_units_alltime: Optional[str]
    max_water_level_observed_date_alltime: datetime
    max_water_level_alltime: Optional[float]
    max_water_level_units_alltime: Optional[str]
    min_water_flow_observed_date_alltime: datetime
    min_water_flow_alltime: Optional[float]
    min_water_flow_units_alltime: Optional[str]
    max_water_flow_observed_date_alltime: datetime
    max_water_flow_alltime: Optional[float]
    max_water_flow_units_alltime: Optional[str]
    max_water_flow_observed_date_alltime: datetime
    max_water_flow_alltime: Optional[float]
    max_water_flow_units_alltime: Optional[str]
    current_water_level_observed_date: datetime
    current_water_level: Optional[float]
    current_water_level_units: Optional[str]
    current_water_flow: Optional[float]
    current_water_flow_units: Optional[str]    

    class Config:
        from_attributes = True

    # def __init__(self, 
    #              station_id: int, 
    #              station_code: str, 
    #              min_water_level_observed_date_alltime: datetime,
    #              min_water_level_alltime: float,
    #              min_water_level_units_alltime: str,
    #              max_water_level_observed_date_alltime: datetime,
    #              max_water_level_alltime: float,
    #              max_water_level_units_alltime: str,
    #              min_water_flow_observed_date_alltime: datetime,
    #              min_water_flow_alltime: float,
    #              min_water_flow_units_alltime: str,
    #              max_water_flow_observed_date_alltime: datetime,
    #              max_water_flow_alltime: float,
    #              max_water_flow_units_alltime: str,
    #              current_water_level_observed_date: datetime,
    #              current_water_level: float,
    #              current_water_level_units: str,
    #              current_water_flow: float,
    #              current_water_flow_units: str):

    #     self.station_id = station_id
    #     self.station_code = station_code
    #     self.min_water_level_observed_date_alltime = min_water_level_observed_date_alltime
    #     self.min_water_level_alltime = min_water_level_alltime
    #     self.min_water_level_units_alltime = min_water_level_units_alltime
    #     self.max_water_level_observed_date_alltime = max_water_level_observed_date_alltime
    #     self.max_water_level_alltime = max_water_level_alltime
    #     self.max_water_level_units_alltime = max_water_level_units_alltime
    #     self.min_water_flow_observed_date_alltime = min_water_flow_observed_date_alltime
    #     self.min_water_flow_alltime = min_water_flow_alltime
    #     self.min_water_flow_units_alltime = min_water_flow_units_alltime
    #     self.max_water_flow_observed_date_alltime = max_water_flow_observed_date_alltime
    #     self.max_water_flow_alltime = max_water_flow_alltime
    #     self.max_water_flow_units_alltime = max_water_flow_units_alltime
    #     self.current_water_level_observed_date = current_water_level_observed_date
    #     self.current_water_level = current_water_level
    #     self.current_water_level_units = current_water_level_units
    #     self.current_water_flow = current_water_flow
    #     self.current_water_flow_units = current_water_flow_units
    #     # self. = 
    #     # self. = 
    #     # self. = 



    # def __repr__(self):
    #     return f"{self.__class__.__name__}({self.id}, {self.station_id}, \
    #     '{self.station_code}', \
    #     {self.min_water_level_observed_date_alltime}, \
    #     {self.min_water_level_observed_date_alltime},\
    #     {self.min_water_level_alltime},\
    #     {self.min_water_level_units_alltime},\
    #     {self.max_water_level_observed_date_alltime},\
    #     {self.max_water_level_alltime},\
    #     {self.max_water_level_units_alltime},\
    #     {self.min_water_flow_observed_date_alltime},\
    #     {self.min_water_flow_alltime},\
    #     {self.min_water_flow_units_alltime},\
    #     {self.max_water_flow_observed_date_alltime},\
    #     {self.max_water_flow_alltime},\
    #     {self.max_water_flow_units_alltime},\
    #     {self.current_water_level_observed_date},\
    #     {self.current_water_level},\
    #     {self.current_water_level_units},\
    #     {self.current_water_flow},\
    #     {self.current_water_flow_units}"
    
