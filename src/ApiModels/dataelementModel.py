from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateDataElement(BaseModel):
    name: str
    datatype: str
    pii: Optional[bool] = False
    isActive: Optional[bool] = True
    isPrimary: Optional[bool] = False
    isUnique: Optional[bool] = False
    isNullable: Optional[bool] = True
    fkTable: Optional[str] = None
    fkColumn: Optional[str] = None
    createdBy: str
    updatedBy: str


class GetDataElement(BaseModel):
    id: int
    name: str
    datatype: str
    datasetName: str
    pii: bool
    isActive: bool
    isPrimary: bool
    isUnique: bool
    isNullable: bool
    fkTable: Optional[str]
    fkColumn: Optional[str]
    createdOn: datetime
    createdBy: str
    updatedOn: datetime
    updatedBy: str

    class Config:
        orm_mode = True
