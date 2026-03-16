from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dbConnection import get_db
from ..ApiModels.datasetModel import CreateDataset, GetDataset, GetDatasetWithElements
from .. import repository
router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.post("/",  summary="Create a new dataset",
              description="Creates a new dataset in the metadata management system.", 
              operation_id="createDataset")
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
    
@router.get("/", response_model=list[GetDataset], summary="Retrieve all datasets",
    description="Fetches all datasets available in the metadata catalog.",
    operation_id="listDatasets")  
def getDatasets(db: Session = Depends(get_db)):
    
    try:
       return repository.getDatasets(db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch dataset: {str(e)}"
        )
    
@router.get("/{datasetId}", response_model=GetDatasetWithElements, summary="Get dataset by ID",
    description="Returns a dataset along with all associated data elements.",
    operation_id="getDatasetById")
def getDataset(datasetId: int, db: Session = Depends(get_db)):

    dataset = repository.getDatasetById(db, datasetId)
    
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    return dataset

    