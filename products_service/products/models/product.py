from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, LargeBinary

from products import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    price = Column(Float)
    new_price = Column(Float)
    description = Column(Text)
    amount = Column(Integer, nullable=False)
    photo = Column(LargeBinary)
    type = Column(Integer, ForeignKey('type.id'))
