from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime
from baskets import db


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    products = Column(String(100))
    total_price = Column(Float)
    date = Column(DateTime, default=datetime.datetime.now)
    payment = Column(Integer)
