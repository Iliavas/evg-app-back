import graphene

import graphql_jwt

from .djangoTypes import TestType

from .models import Test

from .mutations import RegisterUser, CreateTest

class Query(graphene.ObjectType):
    
    testByUser = graphene.List(TestType, token=graphene.String())


    def resolve_testByUser(self, info, token):
        print(info.context.user)
        return Test.objects.filter(user=info.context.user)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    user_auth = RegisterUser.Field()
    create_test = CreateTest.Field()