import graphene

import blog.users.schema
import blog.articles.schema


class Query(blog.users.schema.Query,
            blog.articles.schema.Query):
    pass


class Mutation(blog.users.schema.Mutation,
               blog.articles.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
