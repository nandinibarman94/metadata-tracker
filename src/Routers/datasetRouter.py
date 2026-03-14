from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dbConnection import get_db
from ..ApiModels.datasetModel import CreateDataset
from .. import repository
router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.post("/")
def create_dataset(dataset: CreateDataset, db: Session = Depends(get_db)):

    try:
       repository.CreateDataset(db, dataset.model_dump())
       return {"data":"New dataset created"}

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create dataset: {str(e)}"
        )

    