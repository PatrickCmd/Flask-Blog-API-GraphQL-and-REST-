from flask import Blueprint
from flask_restful import Api

from blog.users.views import (
    UserCreationView, UserSingleView
)

users = Blueprint('users', __name__, url_prefix='/blog_api')
users_api = Api(users)

users_api.add_resource(UserCreationView, '/users')
users_api.add_resource(UserSingleView, '/users/<int:user_id>')
