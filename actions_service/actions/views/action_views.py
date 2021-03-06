from flask import request, Response
from flask_api import status
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import DataError

from actions import db
from actions.models.action import Action
from actions.serializers.action_schema import ActionSchema


def check_authority(view):
    """Decorator for resources"""
    def func_wrapper(*args, **kwargs):
        """wrapper"""
        if request.cookies['admin'] == 'False' and request.method != 'GET':
            return {"error": "Forbidden."}, status.HTTP_403_FORBIDDEN
        return view(*args, **kwargs)
    return func_wrapper


class ActionResource(Resource):
    @check_authority
    def get(self, action_id=None):
        if not action_id:
            actions = Action.query.all()
            actions = ActionSchema(many=True).dump(obj=actions).data
            return actions, status.HTTP_200_OK
        try:
            action = Action.query.get(action_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if action is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        action = ActionSchema().dump(obj=action).data
        return action, status.HTTP_200_OK

    @check_authority
    def delete(self, action_id):
        try:
            action = Action.query.get(action_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if action is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(action)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    @check_authority
    def post(self):
        try:
            data = ActionSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        action = Action(**data)
        db.session.add(action)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)
