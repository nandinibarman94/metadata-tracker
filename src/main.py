from fastapi import FastAPI
from Routers import datasetRouter, dataElementRouter, sourceSystemRouter

tags_metadata = [
    {
        "name": "Datasets",
        "description": "*Operations for managing datasets in the metadata catalog.*"
    },
    {
        "name": "Data Elements",
        "description": "*Operations for managing individual data elements belonging to datasets.*"
    },
    {
        "name": "Source Systems",
        "description": "*Operations for retrieving source systems available in the metadata catalog.*"
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
app.include_router(sourceSystemRouter.router)