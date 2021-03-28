from graphene_django import DjangoObjectType

from .models import Test



class TestType(DjangoObjectType):
    class Meta:
        model = Test

    
