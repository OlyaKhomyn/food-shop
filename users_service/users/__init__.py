from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from users.config.dev_config import DevConfiguration

app = Flask(__name__)

app.config.from_object(DevConfiguration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
from users.models import role, user

API = Api(app, catch_all_404s=True)
CORS(app, supports_credentials=True)

