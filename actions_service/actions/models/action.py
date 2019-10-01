from sqlalchemy import Column, Integer, String, Date

from actions import db


class Action(db.Model):
    id = Column(Integer, primary_key=True)
    discount = Column(Integer)
    type_id = Column(Integer)
    valid_to = Column(Date)
