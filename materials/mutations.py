from .models import Material

from graphene import Mutation
import graphene
from graphql_relay import from_global_id

class CreateDoc(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        content = graphene.String()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(root, cls, info, token, content):
        Material.objects.create(user=info.context.user, content=content)

        return CreateDoc(ok=True)


class UpdateDoc(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        id = graphene.ID()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(root, cls, info, content, id):
        material = Material.objects.get(id=from_global_id(id)[1])

        material.content = content
        material.save()

        return UpdateDoc(ok=True)


class DeleteDoc(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    @classmethod
    def mutate(root, cls, info, id):
        material = Material.objects.get(id=from_global_id(id)[1])
        material.delete()

        return DeleteDoc(ok=True)