from flask_restful import Resource
from flask import Blueprint, jsonify, make_response, request, session
from marshmallow import fields, ValidationError
from flask_api import status
from sqlalchemy.exc import DataError, IntegrityError
from flask_jwt_extended import create_access_token, decode_token

from users.serializers.user_schema import UserSchema, RoleSchema
from users.models.user import User
from users.models.role import Role
from users import db, API
AUTH_BLUEPRINT = Blueprint('users', __name__)


AUTH_TOKEN_KEY = 'auth_token'


class RegisterResource(Resource):
    def post(self):
        try:
            new_user = UserSchema(exclude=['role']).load(request.json).data
        except ValidationError as err:
            return jsonify(err.messages), status.HTTP_400_BAD_REQUEST
        new_user = User(email=new_user['email'], password=new_user['password'],
                        first_name=new_user['first_name'], last_name=new_user['last_name'], role_id=1)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            response = {
                'error': 'Already exists.'
            }
            return response, status.HTTP_400_BAD_REQUEST
        session.permanent = True
        access_token = create_access_token(identity=new_user.user_id, expires_delta=False)
        session[AUTH_TOKEN_KEY] = access_token
        response_obj = jsonify({
            'message': 'Successfully registered.'
        })
        response_obj.set_cookie("admin", str(False))
        return make_response(response_obj, status.HTTP_200_OK)


API.add_resource(RegisterResource, '/users/register')
