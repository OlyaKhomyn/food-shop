from sqlalchemy import Column, Integer, String, UniqueConstraint, LargeBinary
from sqlalchemy.orm import relationship
from products import db


class Type(db.Model):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
    photo = Column(LargeBinary)
    children = relationship("Product", cascade="all,delete")
    __table_args__ = (UniqueConstraint('type'),)
