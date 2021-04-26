from graphene_django import DjangoObjectType

from .models import *
from graphene import relay
import graphene

from graphene_file_upload.scalars import Upload

from collections import namedtuple

from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

        interfaces=(relay.Node,)

class TaskResponseType(graphene.ObjectType):
    Type = graphene.String()
    

    class Meta:
        interfaces = (relay.Node,)


class TestType(DjangoObjectType):
    class Meta:
        model = Test

        interfaces = [relay.Node]

        filter_fields = {
            "name" : ["contains"]
        }
    
    length = graphene.Int()
    tasks_brief = graphene.List(TaskResponseType)

    def resolve_length(self, info):
        return len(self)

    def resolve_tasks_brief(self, info):
        answer = []
        tasksInterface = namedtuple("Task", ["Type", "id"])
        for i in sorted(self.getTasks(), key=lambda x : x.number):
            print(i, i.vName(), i.id, i.number)
            answer.append(tasksInterface(Type=i.vName(), id=i.id))
        print(list(map(lambda x : x.Type, answer))) 
        return answer

    
class ReadAndSayTextType(DjangoObjectType):
    class Meta:
        model = ReadAndSayText

        interfaces = [relay.Node]
    verbose_name = graphene.String()


    def resolve_verbose_name(self, info):
        return "ReadAndSayText"


class ThemeSelectionAndSayType(DjangoObjectType):
    class Meta:
        model = ThemeSelectionAndSay
        interfaces = [relay.Node]

class ThemeSelectionAndSayAnswerType(DjangoObjectType):
    class Meta:
        model = ThemeSelectionAndSayAnswer
        interfaces = [relay.Node]
    
    url = graphene.String()

    def resolve_url(self, info):
        return self.content.url


class AudioDialogType(DjangoObjectType):
    class Meta:
        model = AudioDialog
        interfaces = [relay.Node]
    content = graphene.String()
    title = graphene.String()

    def resolve_content(self, info):
        obj = AudioDialog.objects.get(id=self.id)
        print(self.content)
        finish_link = ""
        try: finish_link = obj.content.url
        except: pass
        return finish_link
    

    def resolve_title(self, info):
        return self.title
    

class AnswerSheetType(DjangoObjectType):
    class Meta:
        model = AnswerSheet

        interfaces = [relay.Node]
    length = graphene.Int()

    answerBreef = graphene.List(TaskResponseType)

    def resolve_answerBreef(self, info):
        answer_interface = namedtuple("Answer", ["id", "Type"])
        res = []
        for i in self.getTasks():
            print(i.task.number, res)
            res.append(answer_interface(id=i.id, Type=i.Type()))
        print(res)
        return res


    def resolve_length(self, info):
        return len(self)


class ReadAndSayAnswerType(DjangoObjectType):
    class Meta:
        model = ReadAndSayAnswer

        interfaces = [relay.Node]
    audioUrl = graphene.String()


    def resolve_audioUrl(self, info):
        return self.content.url


class AudioDialogAnswerType(DjangoObjectType):
    class Meta:
        model = AudioDialogAnswer

        interfaces = [relay.Node]
    audioUrl = graphene.String()

    
    def resolve_audioUrl(self, info):
        return self.content.url