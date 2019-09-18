from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from users import db


class Role(db.Model):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    role_name = Column(String(255), nullable=False)
    role_description = Column(String(255))
    users_roles = relationship('User', backref=backref('role', uselist=False))
