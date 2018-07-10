from datetime import datetime

from blog import db


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def create_category(self):
        db.session.add(self)
        db.commit()

    @staticmethod
    def cattyegor_exists(name):
        user = User.query.filter_by(title=title).first()
    
    @staticmethod
    def get_categories():
        categories = Category.query.all()
        return categories
    
    @staticmethod
    def get_category(cat_id):
        category = Category.query.filter_by(id=cat_id).first()
        return category


class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('articles', lazy='dynamic'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('articles', lazy='dynamic'))
    timestamp = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime)

    def __init__(self, title, content, user_id, category_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.category_id = category_id
        self.timestamp = datetime.now()
        self.update_date = datetime.now()

    def create_article(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_articles():
        articles = Article.query.all()
        return articles
    
    @staticmethod
    def get_article(article_id):
        article = Article.query.filter_by(id=article_id).first()
        return article
        
    @staticmethod
    def get_category_articles(article_id, category_id):
        category_articles = Article.query.filter_by(
            id=article_id, category_id=category_id).all()
        return category_articles
