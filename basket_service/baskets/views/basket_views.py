from flask import request, Response
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser

from baskets import db
from baskets.models.basket import Basket
from baskets.serializers.basket_schema import BasketSchema


class BasketResource(Resource):

    def get(self, basket_id=None):
        if not basket_id:
            args = {
                'user_id': fields.Int(required=True),
                'state': fields.Boolean()
            }
            try:
                args = parser.parse(args, request)
            except HTTPException:
                return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
            baskets = Basket.query.filter(Basket.user_id == args['user_id']).filter(Basket.state == args['state']).all()
            resp = BasketSchema(many=True).dump(obj=baskets).data
            return resp, status.HTTP_200_OK

        try:
            basket = Basket.query.get(basket_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if basket is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        basket = BasketSchema().dump(obj=basket).data
        return basket, status.HTTP_200_OK

    def put(self, basket_id):
        try:
            basket = Basket.query.get(basket_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not basket:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        try:
            data = BasketSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        for key, value in data.items():
            setattr(basket, key, value)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Wrong data."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)

    def delete(self, basket_id):
        try:
            basket = Basket.query.get(basket_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if basket is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(basket)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def post(self):
        try:
            data = BasketSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        basket = Basket(**data)
        db.session.add(basket)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Wrong data."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)
