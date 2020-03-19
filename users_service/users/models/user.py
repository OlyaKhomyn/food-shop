import datetime

import sqlalchemy_utils
from flask_security import UserMixin
from itsdangerous import SignatureExpired, TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from users import db, app, BCRYPT
from users.models.role import Role


class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(sqlalchemy_utils.EmailType, unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
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

    def __init__(self, email, first_name, last_name, role_id, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = BCRYPT.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.role_id = role_id
