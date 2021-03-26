import graphene

from graphene_django import DjangoObjectType



class Query(graphene.ObjectType):
    hello = graphene.Field(graphene.String)

    def resolve_hello(self, res):
        return "hello world"