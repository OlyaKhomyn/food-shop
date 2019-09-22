from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    description = fields.String()
    amount = fields.Integer()
    type = fields.Integer()

    class Meta:
        """Meta class."""
        strict = True


class ProductFromListSchema(Schema):
    id = fields.Integer()
    name = title = fields.String()
    price = fields.Float()

    class Meta:
        """Meta class."""
        strict = True

