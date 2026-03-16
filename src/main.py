from fastapi import FastAPI
from .dbConnection import engine
from .DbModels.base import Base
from .DbModels.sourceSystems import SourceSystems
from .Routers import datasetRouter, dataElementRouter

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Datasets",
        "description": "*Operations for managing datasets in the metadata catalog.*"
    },
    {
        "name": "Data Elements",
        "description": "*Operations for managing individual data elements belonging to datasets.*"
    }
]
app = FastAPI(title="Metadata Management System", 
              openapi_tags=tags_metadata, 
              version="1.0.0",
              swagger_ui_parameters={
                        "docExpansion": "list",
                        "defaultModelsExpandDepth": -1
                                    },
              description= "Metadata Management APIs for managing **datasets** and **data elements**"
            )
app.include_router(datasetRouter.router)
app.include_router(dataElementRouter.router)