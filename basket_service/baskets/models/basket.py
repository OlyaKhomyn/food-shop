"""Field model."""
from sqlalchemy import Column, Integer, Boolean

from baskets import db


class Basket(db.Model):
    """Class used to represent Field model."""
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    user_id = Column(Integer)
    amount = Column(Integer)
    state = Column(Boolean)
