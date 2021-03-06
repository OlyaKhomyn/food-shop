from flask import request, Response, send_file
from flask_api import status
from flask_restful import Resource, HTTPException
from marshmallow import ValidationError, fields
from sqlalchemy.exc import DataError, IntegrityError
from webargs.flaskparser import parser

from products import db
from products.models.product_type import Type
from products.serializers.product_type_schema import ProductTypeSchema
from io import BytesIO


def check_authority(view):
    """Decorator for resources"""
    def func_wrapper(*args, **kwargs):
        """wrapper"""
        if request.cookies['admin'] == 'False' and request.method != 'GET':
            return {"error": "Forbidden."}, status.HTTP_403_FORBIDDEN
        return view(*args, **kwargs)
    return func_wrapper


class TypeResource(Resource):

    ALLOWED_EXTENSIONS = set(['png', 'jpg'])

    @check_authority
    def get(self, type_id=None):
        if not type_id:
            types = Type.query.all()
            types = ProductTypeSchema(many=True).dump(obj=types).data
            return types, status.HTTP_200_OK
        args = {
            'download': fields.Boolean()
        }
        try:
            args = parser.parse(args, request)
        except HTTPException:
            return {"error": "Invalid url"}, status.HTTP_400_BAD_REQUEST
        if args.get('download', None):
            file_data = Type.query.get(type_id)
            response = send_file(BytesIO(file_data.photo), attachment_filename='image.png', as_attachment=True)
            return response
        try:
            type = Type.query.get(type_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if type is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        type = ProductTypeSchema().dump(obj=type).data
        return type, status.HTTP_200_OK

    @check_authority
    def put(self, type_id):
        try:
            prod_type = Type.query.get(type_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if not prod_type:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        try:
            data = ProductTypeSchema().load(request.json).data
        except ValidationError as err:
            return err.messages, status.HTTP_400_BAD_REQUEST
        setattr(prod_type, 'type', data['type'])
        try:
            db.session.commit()
        except IntegrityError:
            return {"error": "Such type already exists."}, status.HTTP_400_BAD_REQUEST
        return Response(status=status.HTTP_200_OK)

    @check_authority
    def delete(self, type_id):
        try:
            prod_type = Type.query.get(type_id)
        except DataError:
            return {"error": "Invalid url."}, status.HTTP_400_BAD_REQUEST
        if prod_type is None:
            return {"error": "Does not exist."}, status.HTTP_400_BAD_REQUEST
        db.session.delete(prod_type)
        db.session.commit()
        return Response(status=status.HTTP_200_OK)

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    @check_authority
    def post(self):
        try:
            data = request.form['type']
            photo = request.files['photo']
        except KeyError:
            return {'error': "Wrong data"}, status.HTTP_400_BAD_REQUEST
        if photo.filename == '':
            return {'error': "No file chosen"}, status.HTTP_400_BAD_REQUEST
        if photo and self.allowed_file(photo.filename):
            prod_type = Type(type=data, photo=photo.read())
            db.session.add(prod_type)
            try:
                db.session.commit()
            except IntegrityError:
                return {"error": "Type already exist."}, status.HTTP_400_BAD_REQUEST
            return Response(status=status.HTTP_200_OK)
        return {'error': "Wrong file format"}, status.HTTP_400_BAD_REQUEST
