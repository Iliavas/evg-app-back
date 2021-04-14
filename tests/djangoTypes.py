from graphene_django import DjangoObjectType

from .models import Test, ReadAndSayText, Task, AudioDialog, AnswerSheet, ReadAndSayAnswer
from graphene import relay
import graphene

from graphene_file_upload.scalars import Upload

from collections import namedtuple



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
        tasksInterface = namedtuple("Task", ["Type", "id"])
        answer = [0 for _ in range(len(self))]
        for i in [*self.readandsaytext_set.all(), 
                  *self.audiodialog_set.all()]:
            print(i, i.vName(), i.id, i.number)
            answer[i.number-1] = tasksInterface(Type=i.vName(), id=i.id)
        print(answer)
        return answer

    
class ReadAndSayTextType(DjangoObjectType):
    class Meta:
        model = ReadAndSayText

        interfaces = [relay.Node]
    verbose_name = graphene.String()


    def resolve_verbose_name(self, info):
        return "ReadAndSayText"


class AudioDialogType(DjangoObjectType):
    class Meta:
        model = AudioDialog

        interfaces = [relay.Node]
    content = graphene.String()
    title = graphene.String()

    def resolve_content(self, info):
        obj = AudioDialog.objects.get(id=self.id)
        print(self.content)
        return obj.content.url
    

    def resolve_title(self, info):
        return AudioDialog.objects.get(id=self.id).title

class AnswerSheetType(DjangoObjectType):
    class Meta:
        model = AnswerSheet

        interfaces = [relay.Node]


class ReadAndSayAnswer(DjangoObjectType):
    class Meta:
        model = ReadAndSayAnswer

        interfaces = [relay.Node]