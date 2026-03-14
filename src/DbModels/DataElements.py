from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from .Base import Base

class DataElements(Base):
    __tablename__ = "dataelements"

    __table_args__ = (
        UniqueConstraint("name", "datasetId", name="UQ_Dataelements"),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    datatype = Column(String, nullable=False)
    datasetId = Column(Integer, ForeignKey("datasets.id"))
    pii = Column(Boolean, default=False)
    isActive = Column(Boolean, default=True)
    isPrimary = Column(Boolean, default=False)
    isUnique = Column(Boolean, default=False)
    isNullable = Column(Boolean, default=True)
    fkTable = Column(String)
    fkColumn = Column(String)
    createdOn = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    createdBy = Column(String, nullable=False)
    updatedOn = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updatedBy = Column(String, nullable=False)

    datasets = relationship("Datasets", back_populates="dataelements")