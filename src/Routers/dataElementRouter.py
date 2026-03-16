from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..dbConnection import get_db
from ..ApiModels.dataElementModel import CreateDataElement, GetDataElement
from .. import repository
from typing import Optional

router = APIRouter(prefix="/elements", tags=["Data Elements"])

@router.post("/", summary="Create a new data element",
    description="Creates a new data element and associates it with a dataset using the provided dataset ID.",
    operation_id="createDataElement")
def createDataElement(element: CreateDataElement, datasetId: int = Query(...), db: Session = Depends(get_db)):
    try:
        createdElement = repository.createDataelement(db, datasetId, element.model_dump())
        if not createdElement:
            raise HTTPException(status_code=404, detail="Dataset not found")
        return {"data": "New data element created"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create data element: {str(e)}"
        )

@router.get("/", response_model=list[GetDataElement], summary="Retrieve data elements",
    description="""
                Returns a list of data elements.  
                Optional filters can be applied to narrow the results.
        """,
        operation_id="listDataElements")
def getDataElements( datasetId: Optional[int] = Query(None), pii: Optional[bool] = Query(None), datatype: Optional[str] = Query(None),   db: Session = Depends(get_db)):
    elements = repository.getDataElements(
        db,
        datasetId=datasetId,
        pii=pii,
        datatype=datatype
    )

    return elements