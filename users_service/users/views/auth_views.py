from flask import Blueprint, jsonify, make_response, request, session
from flask_api import status
from flask_jwt_extended import create_access_token, decode_token
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from users import db, API, BCRYPT
from users.models.user import User
from users.serializers.user_schema import UserSchema

AUTH_BLUEPRINT = Blueprint('users', __name__)


AUTH_TOKEN_KEY = 'auth_token'


class RegisterResource(Resource):
    def post(self):
        try:
            new_user = UserSchema(exclude=['role']).load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        try:
            new_user = User(email=new_user['email'], password=new_user['password'],
                            first_name=new_user['first_name'], last_name=new_user['last_name'], role_id=1)
        except KeyError:
            return {'error': "Missing required field"}
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError as err:
            db.session.emarollback()
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


class LoginResource(Resource):
    def post(self):
        try:
            user_data = UserSchema(exclude=['role']).load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        try:
            user = User.query.filter_by(
                email=user_data['email']
            ).first()
        except KeyError:
            response_obj = {
                'error': 'No email given.'
            }
            return response_obj, status.HTTP_400_BAD_REQUEST
        if user:
            check_user = BCRYPT.check_password_hash(
                user.password, user_data['password']
            )
            if check_user:
                session.permanent = True
                access_token = create_access_token(identity=user.user_id, expires_delta=False)
                session[AUTH_TOKEN_KEY] = access_token
                response_obj = jsonify({
                    'message': 'Successfully logged in.'
                })
                response_obj.set_cookie("admin", str(bool(user.role_id == 2)))
                return make_response(response_obj, status.HTTP_200_OK)
            response_obj = {
                'error': 'Wrong password.'
            }
            return response_obj, status.HTTP_400_BAD_REQUEST
        response_obj = {
            'error': 'No user with this email.'
        }
        return response_obj, status.HTTP_400_BAD_REQUEST


class ProfileResource(Resource):
    """
    Profile Resource.
    """
    def get(self):
        """Get method"""
        try:
            access_token = session[AUTH_TOKEN_KEY]
        except KeyError:
            response_obj = {
                'error': 'Provide a valid auth token.'
            }
            return response_obj, status.HTTP_401_UNAUTHORIZED
        user_info = decode_token(access_token)
        user_id = user_info['identity']
        user = User.query.get(user_id)
        response_obj = UserSchema(strict=True, exclude=['password']).dump(user).data
        resp = make_response(jsonify(response_obj), status.HTTP_200_OK)
        if user.password:
            resp.set_cookie('has_passwd', str(True))
        else:
            resp.set_cookie('has_passwd', str(False))
        return resp


class LogoutResource(Resource):
    """
    Logout Resource
    """
    def post(self):
        """Post method"""
        session.clear()
        response_obj = jsonify({
            'message': 'Successfully logged out.'
        })
        response_obj.delete_cookie('admin')
        return make_response(response_obj, status.HTTP_200_OK)


API.add_resource(RegisterResource, '/users/register')
API.add_resource(LoginResource, '/users/login')
API.add_resource(ProfileResource, '/users/profile')
API.add_resource(LogoutResource, '/users/logout')
