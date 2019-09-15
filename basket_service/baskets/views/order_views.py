from flask import request, Response
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser

from baskets import db
from baskets.models.order import Order
from baskets.serializers.order_schema import OrderSchema


class OrderResource(Resource):

    def get(self, order_id=None):
        if not order_id:
            args = {
                'user_id': fields.Int(required=True)
            }
            try:
                args = parser.parse(args, request)
            except HTTPException:
                return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
            orders = Order.query.filter(Order.user_id == args['user_id']).all()
            resp = OrderSchema(many=True).dump(obj=orders)
            return resp, status.HTTP_200_OK

        try:
            order = Order.query.get(order_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if order is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        order = OrderSchema().dump(obj=order)
        return order, status.HTTP_200_OK

    def put(self, order_id):
        try:
            order = Order.query.get(order_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not order:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        try:
            data = OrderSchema().load(request.json)
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        for key, value in data.items():
            setattr(order, key, value)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Wrong data."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)

    def delete(self, order_id):
        try:
            order = Order.query.get(order_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if order is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(order)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def post(self):
        try:
            data = OrderSchema().load(request.json)
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        order = Order(**data)
        db.session.add(order)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Wrong data."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)
