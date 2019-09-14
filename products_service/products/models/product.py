"""Field model."""
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey

from products import db


class Product(db.Model):
    """Class used to represent Field model."""
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    price = Column(Float)
    description = Column(Text)
    amount = Column(Integer, nullable=False)
    type = Column(Integer, ForeignKey('type.id'))
