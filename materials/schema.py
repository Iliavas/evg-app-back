import graphene

import graphql_jwt
from .gqlTypes import UserType, MaterialType

from graphene import relay
from .mutations import CreateDoc, UpdateDoc, DeleteDoc



class Query(graphene.ObjectType):
    material = relay.Node.Field(MaterialType)

    materials_by_user = graphene.List(MaterialType, token=graphene.String())

    def resolve_materials_by_user(self, info, token):
        return info.context.user.material_set.all()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


    create_doc = CreateDoc.Field()
    update_doc = UpdateDoc.Field()
    delete_doc = DeleteDoc.Field()