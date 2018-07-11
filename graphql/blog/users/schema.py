import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from blog.users.models import User as UserModel


class User(SQLAlchemyObjectType):
    
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        user.create_user()

        return CreateUser(user=user)


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(lambda: User, user_id=graphene.Int())

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()
    
    def resolve_user(self, info, user_id):
        query = User.get_query(info)
        user = query.filter_by(id=user_id).first()
        if not user:
            raise GraphQLError("User not found")
        return user


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
