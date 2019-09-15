from baskets import API
from .basket_views import BasketResource
from .order_views import OrderResource

API.add_resource(BasketResource, '/basket', '/basket/<basket_id>')
API.add_resource(OrderResource, '/order', '/order/<order_id>')
