from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from .Base import Base

class Datasets(Base):
    __tablename__ = "datasets"

    __table_args__ = (
        UniqueConstraint("name", "dbId", name="UQ_Datasets"),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    dbId = Column(Integer, ForeignKey("databases.id"))
    createdOn = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    createdBy = Column(String, nullable=False)
    updatedOn = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updatedBy = Column(String, nullable=False)

    databases = relationship("Databases", back_populates="datasets")
    dataelements = relationship("DataElements", back_populates="datasets", cascade="all, delete")