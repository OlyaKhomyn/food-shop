from marshmallow import Schema, fields


class ProductTypeSchema(Schema):
    id = fields.Integer()
    type = fields.String()

    class Meta:
        """Meta class."""
        strict = True
