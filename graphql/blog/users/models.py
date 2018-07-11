
from flask_bcrypt import generate_password_hash
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship, backref

from blog.database import Base, db_session
from blog.articles.models import Article


class User(Base):
    
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    articles = relationship('Article')

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = generate_password_hash(kwargs.get('password'),
                                               10).decode()

    def __repr__(self):
        return f"<user: {self.username}>"
    
    def create_user(self):
        db_session.add(self)
        db_session.commit()
