"""Field model."""
from sqlalchemy import Column, Integer, String, Boolean

from products import db


class Type(db.Model):
    """Class used to represent Field model."""
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
