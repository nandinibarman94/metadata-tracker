from sqlalchemy.orm import Session
from .DbModels.Datasets import Datasets

def CreateDataset(db: Session, dataset):
    obj = Datasets(**dataset)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj