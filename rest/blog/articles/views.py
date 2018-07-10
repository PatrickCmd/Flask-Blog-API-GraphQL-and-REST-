from flask import make_response, jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args

from blog.articles.models import Category
from blog.articles.schema import CategorySchema


class CategoryCreationView(Resource):
    """ User creation view """

    @use_args(CategorySchema(), locations=('json', 'form'))
    def post(self, args):
        category = Category.cattyegor_exists(args['name'])
        if category:
            response = {
                "message": "category already exists"
            }
            return make_response(jsonify(response), 409)
        category = Category(
            name=args['name'],
            description==args.get('description') or ''
        )
        message = category.create_category()
        response = {
            "message": message
        }
        return make_response(jsonify(response), 201)
    
    def get(self):
        categories = Category.get_categories()
        if categories:
            categories_schema = CategorySchema(many=True)
            categories_serailizer = categories_schema.dump(categories)
            response = {"categories": categories_serailizer}
        else:
            response = {
                "message": "No users created yet"
            }
        return make_response(jsonify(response), 200)


class CategorySingleView(Resource):
    """ Retrieve single user """
    
    def get(self, category_id):
        category = Category.get_category(category_id)
        if category:
            category = CategorySchema()
            category_serializer = category_schema.dump(user)
            response = {"category": category_serializer}
            return make_response(jsonify(response), 200)
        else:
            response = {
                "message": "category not found"
            }
            return make_response(jsonify(response), 404)