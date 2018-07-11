from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.config import Config

db  = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from blog.users import users
    from blog.articles import blog_app

    # register application blueprints
    app.register_blueprint(users)
    app.register_blueprint(blog_app)

    return app