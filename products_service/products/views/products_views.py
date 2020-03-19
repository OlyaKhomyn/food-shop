from flask import request, Response, send_file, jsonify
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser
from io import BytesIO

from products import db
from products.models.product import Product
from products.serializers.product_schema import ProductSchema, ProductFromListSchema


def check_authority(view):
    """Decorator for resources"""
    def func_wrapper(*args, **kwargs):
        """wrapper"""
        if request.cookies['admin'] == 'False' and request.method != 'GET':
            return {"error": "Forbidden."}, status.HTTP_403_FORBIDDEN
        return view(*args, **kwargs)
    return func_wrapper


class ProductResource(Resource):

    ALLOWED_EXTENSIONS = set(['png', 'jpg'])
    @check_authority
    def get(self, product_id=None):
        if not product_id:
            args = {
                'type': fields.List(fields.Int()),
                'product_id': fields.List(fields.Int())
            }
            try:
                args = parser.parse(args, request)
            except HTTPException:
                return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
            if args.get('product_id', None):
                products = []
                for p_id in args['product_id']:
                    element = Product.query.filter_by(id=p_id).first()
                    if not element:
                        resp = {"error": "Does not exist."}
                        status_code = status.HTTP_400_BAD_REQUEST
                        break
                    products.append(element)
                else:
                    resp = ProductFromListSchema(many=True).dump(obj=products).data
                    status_code = status.HTTP_200_OK
                return resp, status_code
            try:
                products = Product.query.filter(Product.type.in_(args['type'])).all()
            except KeyError:
                return {"error": "Missing type id."}, 400
            resp = ProductSchema(many=True).dump(obj=products).data
            return resp, status.HTTP_200_OK
        args = {
            'download': fields.Boolean()
        }
        try:
            args = parser.parse(args, request)
        except HTTPException:
            return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
        if args.get('download', None):
            file_data = Product.query.get(product_id)
            response = send_file(BytesIO(file_data.photo), attachment_filename='image.png',
                                 as_attachment=True)
            return response
        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if product is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        product = ProductSchema().dump(obj=product).data
        return product, status.HTTP_200_OK

    @check_authority
    def put(self, product_id):
        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not product:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        try:
            data = ProductSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        for key, value in data.items():
            setattr(product, key, value)
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Type does not exist."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)

    @check_authority
    def patch(self, product_id):
        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not product:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        product.new_price = request.json['new_price']
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def delete(self, product_id):
        try:
            product = Product.query.get(product_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if product is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(product)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    @check_authority
    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    @check_authority
    def post(self):
        try:
            keys = set(['name', 'price', 'amount', 'type', 'description'])
            attrs = {key: request.form[key] for key in keys}
            data = ProductSchema().load(attrs).data
            photo = request.files['photo']
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        if photo.filename == '':
            return {'error': "No file chosen"}, status.HTTP_400_BAD_REQUEST
        if photo and self.allowed_file(photo.filename):
            product = Product(**data, photo=photo.read())
            db.session.add(product)
            try:
                db.session.commit()
            except IntegrityError:
                return {"error": "Type does not exist."}, status.HTTP_400_BAD_REQUEST
            return Response(status=status.HTTP_200_OK)
        return {'error': "Wrong file format"}, status.HTTP_400_BAD_REQUEST
