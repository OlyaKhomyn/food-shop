from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from products.config.dev_config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# from products.models import product, product_type

API = Api(app, catch_all_404s=True)
CORS(app, supports_credentials=True)

from products.views import resources
