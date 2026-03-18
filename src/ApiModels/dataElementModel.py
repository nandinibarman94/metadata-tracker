from pydantic import BaseModel, model_validator, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum

class CreateDataElement(BaseModel):
    name: str
    datatype: DataType
    description: Optional[str]
    pii: Optional[bool] = False
    isActive: Optional[bool] = True
    isPrimary: Optional[bool] = False
    isUnique: Optional[bool] = None
    isNullable: Optional[bool] = None
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
    datatype: DataType
    datasetName: str
    pii: bool
    isActive: bool
    isPrimary: bool
    isUnique: bool
    isNullable: bool
    createdOn: datetime
    createdBy: str
    updatedOn: datetime
    updatedBy: str

    model_config = ConfigDict(from_attributes=True)

class DataType(str, Enum):
    CHAR = "char"
    VARCHAR = "varchar"
    INTEGER = "integer"
    DECIMAL = "decimal"
    NUMERIC = "numeric"
    FLOAT = "float"
    DOUBLE = "double"
    BOOLEAN = "boolean"
    DATE = "date"
    TIME = "time"
    TIMESTAMP = "timestamp"
    UUID = "uuid"