import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from blog.articles.models import(
    Category as CategoryModel,
    Article as ArticleModel
)


class Category(SQLAlchemyObjectType):
    
    class Meta:
        model = CategoryModel


class CreateCategory(graphene.Mutation):
    
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False)
    category = graphene.Field(Category)

    def mutate(self, info, **kwargs):
        category = CategoryModel(**kwargs)
        category.create_category()

        return CreateCategory(category=category)

class Article(SQLAlchemyObjectType):
    
    class Meta:
        model = ArticleModel


class CreateArticle(graphene.Mutation):
    
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=False)
        user_id = graphene.Int(required=True)
        category_id = graphene.Int(required=True)
    article = graphene.Field(Article)

    def mutate(self, info, **kwargs):
        article = ArticleModel(**kwargs)
        article.create_article()

        return CreateArticle(article=article)


class Query(graphene.ObjectType):
    categories = graphene.List(Category)
    articles = graphene.List(Article)
    category = graphene.Field(lambda: Category, category_id=graphene.Int())
    article = graphene.Field(lambda: Article, article_id=graphene.Int())
    user_articles = graphene.List(lambda: Article, user_id=graphene.Int())

    def resolve_categories(self, info):
        query = Category.get_query(info)
        return query.all()
    
    def resolve_category(self, info, category_id):
        query = Category.get_query(info)
        category = query.filter_by(id=category_id).first()
        if not category:
            raise GraphQLError("Category not found")
        return category
    
    def resolve_articles(self, info):
        query = Article.get_query(info)
        return query.all()
    
    def resolve_article(self, info, article_id):
        query = Article.get_query(info)
        article = query.filter_by(id=article_id).first()
        if not article:
            raise GraphQLError("Article not found")
        return article
    
    def resolve_user_articles(self, info, user_id):
        query = Article.get_query(info)
        articles = query.filter_by(user_id=user_id).all()
        if not articles:
            raise GraphQLError("User has no articles yet")
        return articles


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_article = CreateArticle.Field()
