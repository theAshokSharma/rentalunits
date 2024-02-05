from fastapi import FastAPI
import uvicorn
import os

from rentalunits import log, config
from rentalunits.db.database import create_db_and_tables
from rentalunits.routers.v1 import propertyinfo_service

app = FastAPI()
create_db_and_tables()

app.include_router(propertyinfo_service.router)


@app.get("/")
def root():
    return {"message": "RentalUnits: 1.0.0.0"}


if __name__ == '__main__':
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=2428,
                log_level="info",
                reload=True,
                ssl_keyfile="ssl/localhost.key",
                ssl_certfile="ssl/localhost.crt")
    print("running")
