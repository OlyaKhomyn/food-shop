from products import API
from .products_views import ProductResource
from .product_type_views import TypeResource

API.add_resource(ProductResource, '/product', '/product/<product_id>')
API.add_resource(TypeResource, '/type', '/type/<type_id>')
