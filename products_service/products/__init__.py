from flask import Flask
from flask_restful import Api
from flask_cors import CORS


APP = Flask(__name__)
API = Api(APP, catch_all_404s=True)
CORS(APP, supports_credentials=True)
