from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from users.config.dev_config import DevConfiguration

app = Flask(__name__)

app.config.from_object(DevConfiguration)
db = SQLAlchemy(app)
BCRYPT = Bcrypt(app)

migrate = Migrate(app, db)
from users.models import role, user

API = Api(app, catch_all_404s=True)
CORS(app, supports_credentials=True)
JWT = JWTManager(app)

from users.views.auth_views import AUTH_BLUEPRINT
app.register_blueprint(AUTH_BLUEPRINT)
