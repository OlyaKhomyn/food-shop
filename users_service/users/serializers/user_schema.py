from marshmallow import Schema, fields


class RoleSchema(Schema):
    id = fields.Integer(dump_only=True)
    role_name = fields.Str()
    role_description = fields.Str()

    class Meta:
        """Meta class."""
        strict = True


class UserSchema(Schema):
    user_id = fields.Integer(dump_only=True)
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    password = fields.Str()
    role_id = fields.Integer()
    role = fields.Nested(RoleSchema)
    create_date = fields.DateTime(dump_only=True)
    update_date = fields.DateTime()

    class Meta:
        """Meta class."""
        strict = True

