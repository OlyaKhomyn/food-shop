"""Config."""
LOCKAL_DB = 'postgres://postgres:postgres@localhost:5432/basket'
DOCKER_DB = 'postgresql://postgres:mysecretpassword@db:5432/basket'


class Config:
    """Implementation of Configuration class."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DOCKER_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = True
