from fastapi import FastAPI
from .dbConnection import engine
from .DbModels.Base import Base
from .DbModels.Databases import Databases
from .DbModels.DataElements import DataElements
from .Routers import datasetRouter

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Metadata Management System")
app.include_router(datasetRouter.router)