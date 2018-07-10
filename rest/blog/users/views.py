from flask import make_response, jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args

from blog.users.models import User
from blog.users.schema import UserSchema


class UserCreationView(Resource):
    """ User creation view """

    @use_args(UserSchema(), locations=('json', 'form'))
    def post(self, args):
        user = User.user_exists(args['username'], args['email'])
        if user:
            response = {
                "message": "User with that username or email already exists"
            }
            return make_response(jsonify(response), 409)
        user = User(
            username=args['username'],
            email=args['email'],
            password=args['password']
        )
        message = user.create_user()
        response = {
            "message": message
        }
        return make_response(jsonify(response), 201)
    
    def get(self):
        users = User.get_users()
        if users:
            users_schema = UserSchema(many=True)
            users_serailizer = users_schema.dump(users)
            response = {"users": users_serailizer}
        else:
            response = {
                "message": "No users created yet"
            }
        return make_response(jsonify(response), 200)


class UserSingleView(Resource):
    """ Retrieve single user """
    
    def get(self, user_id):
        user = User.get_user(user_id)
        if user:
            user_schema = UserSchema()
            user_serializer = user_schema.dump(user)
            response = {"user": user_serializer}
            return make_response(jsonify(response), 200)
        else:
            response = {
                "message": "User not found"
            }
            return make_response(jsonify(response), 404)