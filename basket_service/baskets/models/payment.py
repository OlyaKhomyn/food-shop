from sqlalchemy import Column, Integer, String
from baskets import db


class Payment(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    phone = Column(String(10))
    city = Column(String(100))
    department = Column(Integer)
