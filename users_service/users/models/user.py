from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
import sqlalchemy_utils
import datetime
from flask_security import UserMixin
from itsdangerous import SignatureExpired, TimedJSONWebSignatureSerializer as Serializer

from users import db, app


class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(sqlalchemy_utils.EmailType, unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    google_id = Column(String(255), unique=True, nullable=True, default=None)
    password = Column(String(255), nullable=True, default=None)
    role_id = Column(Integer, ForeignKey('role.id'))
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_date = Column(DateTime, nullable=False, default=datetime.datetime.now())

    def get_reset_token(self, expires_sec=7200):
        """Create reset password token"""
        serial = Serializer(app.config.get('SECRET_KEY'), expires_sec)
        return serial.dumps({'user_id': self.user_id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """Check reset password token"""
        serial = Serializer(app.config.get('SECRET_KEY'))
        try:
            user_id = serial.loads(token)['user_id']
        except SignatureExpired:
            return None
        return User.query.get(user_id)
