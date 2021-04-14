import graphene_django

from graphene import relay

from .models import Material

from django.contrib.auth.models import User

class MaterialType(graphene_django.DjangoObjectType):
    class Meta:
        model = Material
        interfaces = [relay.Node]

class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User