from marshmallow import Schema, fields, post_load, pre_dump


class OrderSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    products = fields.List(fields.Integer())
    total_price = fields.Float()
    date = fields.Date()
    payment = fields.Integer()

    @post_load
    def convert_list_from_str(self, data, **kwargs):
        """Converts into list from string."""
        if 'products' in data:
            data['products'] = ",".join(map(str, data['products']))
        return data

    @pre_dump
    def convert_str_from_list(self, data, **kwargs):
        """Converts into string from list."""
        if data:
            data.products = list(map(int, data.products.split(',')))
        return data

    class Meta:
        """Meta class."""
        strict = True
