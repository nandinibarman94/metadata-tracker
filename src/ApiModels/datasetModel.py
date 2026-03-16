from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from .dataElementModel import GetDataElement

class CreateDataset(BaseModel):
    name: str
    description: Optional[str] = None
    sourceSystemId: int
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
    
    model_config = ConfigDict(from_attributes=True)

class GetDatasetWithElements(GetDataset):
    dataelements: list[GetDataElement] = []

    model_config = ConfigDict(from_attributes=True)
