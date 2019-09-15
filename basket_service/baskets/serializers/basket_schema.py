from marshmallow import Schema, fields


class BasketSchema(Schema):
    id = fields.Integer()
    product_id = fields.Integer()
    user_id = fields.Integer()
    amount = fields.Integer()
    state = fields.Boolean()

    class Meta:
        """Meta class."""
        strict = True
