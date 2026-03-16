from sqlalchemy.orm import Session, joinedload
from DbModels.datasets import Datasets
from DbModels.dataElements import DataElements
from datetime import datetime,timezone
from typing import Optional

def createDataset(db: Session, dataset):
    dataset = Datasets(
        **dataset,
        createdOn= datetime.now(timezone.utc),
        updatedOn= datetime.now(timezone.utc)
        )
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset

def getDatasets(db: Session):
    return db.query(Datasets).options(joinedload(Datasets.sourcesystems)).all()

def getDatasetById(db: Session, datasetId: int):
    dataset = (
        db.query(Datasets)
        .options(
            joinedload(Datasets.sourcesystems),
            joinedload(Datasets.dataelements)
        )
        .filter(Datasets.id == datasetId)
        .first()
    )

    if not dataset:
        return None
    
    return dataset

def createDataelement(db: Session, datasetId: int, elementData):
    dataset = db.query(Datasets).filter(Datasets.id == datasetId).first()
    if not dataset:
        return None

    dataelement = DataElements(
        **elementData,
        datasetId=datasetId,
        createdOn= datetime.now(timezone.utc),
        updatedOn= datetime.now(timezone.utc)
    )
    db.add(dataelement)
    db.commit()
    db.refresh(dataelement)
    return dataelement

def getDataElements(db: Session, datasetId: Optional[int] = None, pii: Optional[bool] = None, datatype: Optional[str] = None):
    query = db.query(DataElements)
    if datasetId is not None:
        query = query.filter(DataElements.datasetId == datasetId)
    if pii is not None:
        query = query.filter(DataElements.pii == pii)
    if datatype is not None:
        query = query.filter(DataElements.datatype == datatype)
    return query.all()