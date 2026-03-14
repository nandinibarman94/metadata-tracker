from fastapi import FastAPI
from .dbConnection import engine
from .Models.Base import Base
from .Models.Databases import Databases
from .Models.Datasets import Datasets
from .Models.DataElements import DataElements

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Metadata Management System")