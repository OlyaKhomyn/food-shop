import os
from users.config.base_config import Configuration

BASEDIR = os.path.abspath(os.path.dirname(__file__))
POSTGRES_LOCAL_BASE = 'postgres://postgres:postgres@localhost:5432/users'
Docker_DB = 'postgresql://postgres:mysecretpassword@db:5432/users'


class DevConfiguration(Configuration):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = Docker_DB

    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = False
    REMEMBER_COOKIE_DURATION = 600
    SESSION_COOKIE_DOMAIN = '127.0.0.1'

    SECRET_KEY = 'very_secret'
