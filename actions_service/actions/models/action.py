from sqlalchemy import Column, Integer, String, Date

from actions import db


class Action(db.Model):
    id = Column(Integer, primary_key=True)
    discount = Column(Integer)
    type_ids = Column(String(100))
    valid_to = Column(Date)
