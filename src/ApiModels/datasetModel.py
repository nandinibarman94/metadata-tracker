from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .dataelementModel import GetDataElement

class CreateDataset(BaseModel):
    name: str
    description: Optional[str] = None
    dbId: int
    createdBy: str
    updatedBy: str

class GetDataset(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    sourceSystemName: str
    createdOn: datetime
    createdBy: str
    updatedOn: datetime
    updatedBy: str
    
    class Config:
        from_attributes = True

class GetDatasetWithElements(GetDataset):
    dataelements: list[GetDataElement] = []

    class Config:
        from_attributes = True
