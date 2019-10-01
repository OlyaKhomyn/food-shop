from flask import request, Response
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser

from baskets import db
from baskets.models.payment import Payment
from baskets.models.order import Order

from baskets.serializers.order_schema import OrderSchema


class OrderResource(Resource):

    def get(self, order_id=None):
        if not order_id:
            args = {
                'user_id': fields.Int()
            }
            try:
                args = parser.parse(args, request)
            except HTTPException:
                return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
            try:
                orders = Order.query.filter(Order.user_id == args['user_id']).all()
            except KeyError:
                return {"error": "user_id is required"}, status.HTTP_400_BAD_REQUEST
            for order in orders:
                payment = Payment.query.get(order.payment)
                order.payment_info = payment
            resp = OrderSchema(many=True).dump(obj=orders).data
            return resp, status.HTTP_200_OK

        try:
            order = Order.query.get(order_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if order is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        payment = Payment.query.get(order.payment)
        order.payment_info = payment
        order = OrderSchema().dump(obj=order).data
        return order, status.HTTP_200_OK

    def delete(self, order_id):
        try:
            order = Order.query.get(order_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if order is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        payment = Payment.query.get(order.payment)
        db.session.delete(payment)
        db.session.delete(order)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def post(self):
        try:
            data = OrderSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        payment = Payment(**data.pop('payment_info'))
        db.session.add(payment)
        db.session.commit()
        data['payment'] = payment.id
        order = Order(**data)
        db.session.add(order)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Wrong data."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)
