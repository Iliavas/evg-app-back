import graphene

from django.contrib.auth.models import User


class RegisterUser(graphene.Mutation):

    ok = graphene.Boolean()

    class Arguments:
        username = graphene.String()
        password = graphene.String()


    @classmethod
    def mutate(root, info, username, password):
        User.objects.create_user(username=username, password=password)
        return RegisterUser(ok=True)