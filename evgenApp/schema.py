import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "hello world"

class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)