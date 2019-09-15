from baskets import API
from .basket_views import BasketResource

API.add_resource(BasketResource, '/basket', '/basket/<basket_id>')
