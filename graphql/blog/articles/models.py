from datetime import datetime

from sqlalchemy import (Column, String, Integer, Text, DateTime, ForeignKey)
from sqlalchemy.orm import relationship

from blog.database import Base, db_session


class Category(Base):
    
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def create_category(self):
        db_session.add(self)
        db_session.commit()
        return "Category added successfully"


class Article(Base):
    
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')
    timestamp = Column(DateTime, nullable=False)
    update_date = Column(DateTime)

    def __init__(self, title, content, user_id, category_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.category_id = category_id
        self.timestamp = datetime.now()
        self.update_date = datetime.now()

    def create_article(self):
        db_session.add(self)
        db_session.commit()
        return "Article added successfully"
