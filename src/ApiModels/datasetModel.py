from pydantic import BaseModel
from typing import Optional

class CreateDataset(BaseModel):
    name: str
    description: Optional[str] = None
    dbId: int
    createdBy: str
    updatedBy: str