from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Datasets(Base):
    __tablename__ = "datasets"

    __table_args__ = (
        UniqueConstraint("name", "sourceSystemId", name="UQ_Datasets"),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    sourceSystemId = Column(Integer, ForeignKey("sourcesystems.id"))
    createdOn = Column(DateTime, nullable=False)
    createdBy = Column(String, nullable=False)
    updatedOn = Column(DateTime, nullable=False)
    updatedBy = Column(String, nullable=False)

    sourcesystems = relationship("SourceSystems", back_populates="datasets")
    dataelements = relationship("DataElements", back_populates="datasets", cascade="all, delete")

    @property
    def sourceSystemName(self):
        return self.sourcesystems.name