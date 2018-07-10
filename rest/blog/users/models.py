from flask_bcrypt import generate_password_hash
from flask_sqlalchemy import sqlalchemy as sql
from blog import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, 10).decode()

    def __repr__(self):
        return f"<user: {self.username}>"
    
    def create_user(self):
        db.session.add(self)
        db.session.commit()
        return "User successfully registered"
    
    @staticmethod
    def get_users():
        users = User.query.all()
        return users
    
    @staticmethod
    def user_exists(username, email):
        user = User.query.filter(sql.or_(User.username==username,
                                 User.email==email)).first()
        return user
    
    @staticmethod
    def get_user(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user
