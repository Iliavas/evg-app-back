import graphene

from django.contrib.auth.models import User

from .models import Test

from .djangoTypes import TestType

class RegisterUser(graphene.Mutation):

    ok = graphene.Boolean()

    class Arguments:
        username = graphene.String()
        password = graphene.String()


    @classmethod
    def mutate(cls, root, info, username, password):
        User.objects.create_user(username=username, password=password)
        return RegisterUser(ok=True)



class CreateTest(graphene.Mutation):
    test = graphene.Field(TestType)

    class Arguments:
        name = graphene.String()
        token = graphene.String()
    

    @classmethod
    def mutate(cls, root, info, name, token):
        print(root, info)
        test = Test.objects.create(user=info.context.user, name=name)
        return CreateTest(test=test)