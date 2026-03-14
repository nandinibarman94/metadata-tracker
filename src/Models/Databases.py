from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from .Base import Base

class Databases(Base):
    __tablename__ = "databases"

    __table_args__ = (
        UniqueConstraint("name", name="UQ_Databases"),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    createdOn = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    createdBy = Column(String, nullable=False)
    updatedOn = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updatedBy = Column(String, nullable=False)

    datasets = relationship("Datasets", back_populates="databases")