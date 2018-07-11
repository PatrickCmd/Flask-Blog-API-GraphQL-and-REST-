from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

from blog.config import Config
from blog.schema import schema

from blog.database import db_session


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.add_url_rule(
        '/blog_api',
        view_func=GraphQLView.as_view(
            'blog_api',
            schema=schema,
            graphiql=True # for having GraphiQL interface
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app