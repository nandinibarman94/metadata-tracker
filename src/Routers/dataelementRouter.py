from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..dbConnection import get_db
from ..ApiModels.dataelementModel import CreateDataElement, GetDataElement
from .. import repository
from typing import Optional

router = APIRouter(prefix="/elements", tags=["Data Elements"])

@router.post("/")
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

@router.get("/", response_model=list[GetDataElement])
def getDataElements( datasetId: Optional[int] = Query(None), pii: Optional[bool] = Query(None), datatype: Optional[str] = Query(None),   db: Session = Depends(get_db)):
    elements = repository.getDataElements(
        db,
        datasetId=datasetId,
        pii=pii,
        datatype=datatype
    )

    return elements