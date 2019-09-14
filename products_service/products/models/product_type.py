"""Field model."""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from products import db


class Type(db.Model):
    """Class used to represent Field model."""
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
    children = relationship("Product", cascade="all,delete")
    __table_args__ = (UniqueConstraint('type'),)
