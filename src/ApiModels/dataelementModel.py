from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime

class CreateDataElement(BaseModel):
    name: str
    datatype: str
    description: Optional[str]
    pii: Optional[bool] = False
    isActive: Optional[bool] = True
    isPrimary: Optional[bool] = False
    isUnique: Optional[bool] = None
    isNullable: Optional[bool] = None
    referenceTableName: Optional[str] = None
    referenceColumnName: Optional[str] = None
    createdBy: str
    updatedBy: str

    @model_validator(mode="before")
    def set_primary_defaults(cls, values):
        is_primary = values.get("isPrimary")
        is_unique = values.get("isUnique")
        is_nullable = values.get("isNullable")

        if is_primary:
            if is_unique is None:
                values["isUnique"] = True
            if is_nullable is None:
                values["isNullable"] = False

            if values["isUnique"] is not True:
                raise ValueError("Primary key columns must be unique (isUnique=True).")
            if values["isNullable"] is not False:
                raise ValueError("Primary key columns cannot be nullable (isNullable=False).")

        return values


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
    referenceTableName: Optional[str]
    referenceColumnName: Optional[str]
    createdOn: datetime
    createdBy: str
    updatedOn: datetime
    updatedBy: str

    class Config:
        from_attributes = True
