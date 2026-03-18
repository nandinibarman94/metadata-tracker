from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbConnection import get_db
from ApiModels.sourceSystemModel import GetSourceSystem
import repository
router = APIRouter(prefix="/sourcesystems", tags=["Source Systems"])

@router.get("/", response_model=list[GetSourceSystem], summary="Retrieve all sourcesystems",
    description="Fetches all source systems available in the metadata catalog.",
    operation_id="listSourceSystems")  
def getSourceSystems(db: Session = Depends(get_db)):
    
    try:
       return repository.getSourceSystems(db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch sourcesystems: {str(e)}"
        )