from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from .Base import Base

class SourceSystems(Base):
    __tablename__ = "sourcesystems"

    __table_args__ = (
        UniqueConstraint("name","owningApplication", name="UQ_SourceSystem"),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owningApplication = Column(String, nullable=False)
    createdOn = Column(DateTime, nullable=False)
    createdBy = Column(String, nullable=False)
    updatedOn = Column(DateTime, nullable=False)
    updatedBy = Column(String, nullable=False)

    datasets = relationship("Datasets", back_populates="sourcesystems")