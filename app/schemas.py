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