from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.config import Config

db  = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from blog.users import users

    # register application blueprints
    app.register_blueprint(users)
    
    return app