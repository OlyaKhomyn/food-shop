from actions import API
from .action_views import ActionResource

API.add_resource(ActionResource, '/action', '/action/<action_id>')
