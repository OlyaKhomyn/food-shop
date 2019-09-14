"""Config."""


class Config:
    """Implementation of Configuration class."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/products'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
