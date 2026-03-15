from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dbConnection import get_db
from ..ApiModels.datasetModel import CreateDataset, GetDataset, GetDatasetWithElements
from .. import repository
router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.post("/")
def createDataset(dataset: CreateDataset, db: Session = Depends(get_db)):

    try:
       repository.createDataset(db, dataset.model_dump())
       return {"data":"New dataset created"}

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create dataset: {str(e)}"
        )
    
@router.get("/", response_model=list[GetDataset])  
def getDatasets(db: Session = Depends(get_db)):
    
    try:
       return repository.getDatasets(db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch dataset: {str(e)}"
        )
    
@router.get("/{datasetId}", response_model=GetDatasetWithElements)
def getDataset(datasetId: int, db: Session = Depends(get_db)):

    dataset = repository.getDatasetById(db, datasetId)
    
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    return dataset

    