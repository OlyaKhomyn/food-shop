from marshmallow import Schema, fields, post_load, pre_dump


class ActionSchema(Schema):
    id = fields.Integer()
    discount = fields.Float()
    type_ids = fields.List(fields.Integer())
    valid_to = fields.Date()

    @post_load
    def convert_list_from_str(self, data, **kwargs):
        """Converts into list from string."""
        if 'type_ids' in data:
            data['type_ids'] = ",".join(map(str, data['type_ids']))
        return data

    @pre_dump
    def convert_str_from_list(self, data, **kwargs):
        """Converts into string from list."""
        if data:
            data.type_ids = list(map(int, data.type_ids.split(',')))
        return data

    class Meta:
        """Meta class."""
        strict = True
