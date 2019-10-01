from marshmallow import Schema, fields


class PaymentSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    phone = fields.String(validate=lambda x: x.isnumeric())
    city = fields.String()
    department = fields.Integer()

    class Meta:
        """Meta class."""
        strict = True
