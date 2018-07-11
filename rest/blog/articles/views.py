from flask import make_response, jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args

from blog.articles.models import Category, Article
from blog.articles.schema import CategorySchema, ArticleSchema


class CategoryCreationView(Resource):
    """ User creation view """

    @use_args(CategorySchema(), locations=('json', 'form'))
    def post(self, args):
        category = Category.category_exists(args['name'])
        if category:
            response = {
                "message": "category already exists"
            }
            return make_response(jsonify(response), 409)
        category = Category(
            name=args['name'],
            description=args.get('description') or ''
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
                "message": "No categories created yet"
            }
        return make_response(jsonify(response), 200)


class CategorySingleView(Resource):
    """ Retrieve single user """
    
    def get(self, category_id):
        category = Category.get_category(category_id)
        if category:
            category_schema = CategorySchema()
            category_serializer = category_schema.dump(category)
            response = {"category": category_serializer}
            return make_response(jsonify(response), 200)
        else:
            response = {
                "message": "category not found"
            }
            return make_response(jsonify(response), 404)

class ArticleCreationView(Resource):
    """ Article creation view """

    @use_args(ArticleSchema(), locations=('json', 'form'))
    def post(self, args):
        article = Article(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            category_id=args['category_id']
        )
        message = article.create_article()
        response = {
            "message": message
        }
        return make_response(jsonify(response), 201)
    
    def get(self):
        articles = Article.get_articles()
        if articles:
            articles_schema = ArticleSchema(many=True)
            articles_serailizer = articles_schema.dump(articles)
            response = {"articles": articles_serailizer}
        else:
            response = {
                "message": "No articles created yet"
            }
        return make_response(jsonify(response), 200)


class ArticleSingleView(Resource):
    """ Retrieve single article """
    
    def get(self, article_id):
        article = Article.get_article(article_id)
        if article:
            article_schema = ArticleSchema()
            article_serializer = article_schema.dump(article)
            response = {"article": article_serializer}
            return make_response(jsonify(response), 200)
        else:
            response = {
                "message": "Article not found"
            }
            return make_response(jsonify(response), 404)


class UserArticlesView(Resource):
    """ Retrieve users articles """
    
    def get(self, user_id):
        user_articles = Article.get_user_articles(user_id)
        if user_articles:
            user_articles_schema = ArticleSchema(many=True)
            articles_serializer = user_articles_schema.dump(user_articles)
            response = {"user_articles": articles_serializer}
            return make_response(jsonify(response), 200)
        else:
            response = {
                "message": "User has no Articles yet"
            }
            return make_response(jsonify(response), 200)