import graphene
import materials.schema



class Query(materials.schema.Query, graphene.ObjectType):
  hello = graphene.String()


  def resolve_hello(self, info):
    return "hello world"


class Mutation(materials.schema.Mutation, graphene.ObjectType):
  pass


schema = graphene.Schema(query=Query, mutation=Mutation)