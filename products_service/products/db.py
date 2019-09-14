from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from products import APP
from products.config.dev_config import DevelopmentConfig

APP.config.from_object(DevelopmentConfig)
DB = SQLAlchemy(APP)


MIGRATE = Migrate(APP, DB)
