from fastapi import FastAPI
from datetime import datetime
from .routers import user, auth, station, waterreport
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(station.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(waterreport.WaterLevelRouter)
app.include_router(waterreport.WaterReport)
app.include_router(waterreport.CurrentWaterReading)

@app.get("/")
def root():
    return {"message": f"New API!!! {datetime.now()}"}


