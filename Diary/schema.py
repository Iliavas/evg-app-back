import graphene
import graphene_django

from .models import Profile, Mark

# Create a Query type
class Query(ObjectType):
    Marks = graphene.List(MarkType)
    def getAllSubjectMarks(self, info, **kwargs):
        token = Profile.objects.get(**fields).token #gets user token from django.contrib.auth.models.User
        subject = kwargs.get('subject') # gets subject from function input
        if token is not None and subject is not None:
            return Lesson.objects.get(user=token, lesson=subject)
        return None

    def getAllMarks(self, info, **kwargs):
        token = Profile.objects.get(**fields).token #gets user token from django.contrib.auth.models.User
        if token is not None:
            return Lesson.objects.get(user=token)
        return None

class Marks(graphene_django.DjangoObjectType):
    class Meta:
        model = Marks


class putMark(graphene.Mutation):
    ok = graphene.Boolean()
    
    class Arguments:
        username = graphene.String()
        date = graphene.Date()
        mark = graphene.Int()

    @classmethod
    def mutate(cls, root, info, field):
        Mark.objects.create(user=username, date=date, mark=)
        return CreateMark(ok=True)


class Mutation(graphene.ObjectType):
    create_model_mutation = CreateMark.Field()