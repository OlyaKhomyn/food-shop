"""Field model."""
from sqlalchemy import Column, Integer, String, Float

from baskets import db


class Order(db.Model):
    """Class used to represent Field model."""
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    user_id = Column(Integer)
    products = Column(String(100))
    total_price = price = Column(Float)
