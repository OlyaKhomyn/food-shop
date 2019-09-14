from flask import request, Response
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser

from products import db
from products.models.product import Product
from products.serializers.product_schema import ProductSchema


class ProductResource(Resource):
    def get(self, product_id=None):
        if not product_id:
            args = {
                'type': fields.List(fields.Int())
            }
            try:
                args = parser.parse(args, request)
            except HTTPException:
                return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
            products = Product.query.filter(Product.type.in_(args['type'])).all()
            resp = ProductSchema(many=True).dump(obj=products)
            return resp, status.HTTP_200_OK

        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if product is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        field = ProductSchema().dump(obj=product)
        return field, status.HTTP_200_OK

    def put(self, product_id):
        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not product:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        try:
            data = ProductSchema().load(request.json)
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        for key, value in data.items():
            setattr(product, key, value)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Type does not exist."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)

    def delete(self, product_id):
        try:
            product = Product.query.get(product_id)
        except DataError as err:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if product is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(product)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def post(self):
        try:
            data = ProductSchema().load(request.json)
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        product = Product(**data)
        db.session.add(product)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Type does not exist."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)
