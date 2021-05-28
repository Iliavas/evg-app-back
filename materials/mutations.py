from .models import Material

from graphene import Mutation
import graphene
from graphql_relay import from_global_id

from django.contrib.auth.models import User

from .gqlTypes import MaterialType

class CreateDoc(graphene.Mutation):
    class Arguments:
        token = graphene.String()
        content = graphene.String()
        name = graphene.String()
        state = graphene.String()
    
    document = graphene.Field(MaterialType)

    @classmethod
    def mutate(root, cls, info, token, content, name, state):
        doc = Material.objects.create(
            user=info.context.user, 
            content=content, 
            name=name,
            state=state
            )

        return CreateDoc(document=doc)


class UpdateDoc(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        state = graphene.String()
        name = graphene.String()
        id = graphene.ID()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(root, cls, info, content, id):
        material = Material.objects.get(id=from_global_id(id)[1])

        material.content = content
        material.state = state
        material.name = name
        material.save()

        return UpdateDoc(ok=True)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, username, password):
        User.objects.create_user(username=username, password=password)
        return CreateUser(ok=True)

class DeleteDoc(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    @classmethod
    def mutate(root, cls, info, id):
        material = Material.objects.get(id=from_global_id(id)[1])
        material.delete()

        return DeleteDoc(ok=True)