from marshmallow import Schema, fields


class ActionSchema(Schema):
    id = fields.Integer()
    discount = fields.Float()
    type_id = fields.Integer()
    valid_to = fields.Date()

    class Meta:
        """Meta class."""
        strict = True
