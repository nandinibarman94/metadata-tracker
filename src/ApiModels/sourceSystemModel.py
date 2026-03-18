from pydantic import BaseModel, ConfigDict
from datetime import datetime

class GetSourceSystem(BaseModel):
    id : int
    name: str
    owningApplication: str
    createdOn: datetime
    createdBy: str
    updatedOn: datetime
    updatedBy: str
    
    model_config = ConfigDict(from_attributes=True)