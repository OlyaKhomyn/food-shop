from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from baskets.config.dev_config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
from baskets.models import basket, order, payment

API = Api(app, catch_all_404s=True)
CORS(app, supports_credentials=True)

from baskets.views import resources
