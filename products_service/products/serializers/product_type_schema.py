from marshmallow import Schema, fields


class ProductTypeSchema(Schema):
    id = fields.Integer()
    type = fields.String(required=True)

    class Meta:
        """Meta class."""
        strict = True
