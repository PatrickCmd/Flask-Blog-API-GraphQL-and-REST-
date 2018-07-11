from flask import Blueprint
from flask_restful import Api

from blog.articles.views import (
    CategoryCreationView, CategorySingleView,
    ArticleCreationView, ArticleSingleView,
    UserArticlesView
)
blog_app = Blueprint('blog_app', __name__, url_prefix='/blog_api')
blog_api = Api(blog_app)

blog_api.add_resource(CategoryCreationView, '/categories')
blog_api.add_resource(CategorySingleView,
                            '/categories/<int:category_id>')

blog_api.add_resource(ArticleCreationView, '/articles')
blog_api.add_resource(ArticleSingleView,
                            '/articles/<int:article_id>')
blog_api.add_resource(UserArticlesView,
                            '/users/<int:user_id>/articles')
