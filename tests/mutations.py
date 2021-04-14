import graphene

from django.contrib.auth.models import User

from .models import Test, ReadAndSayText, AudioDialog, AnswerSheet

from .djangoTypes import TestType, AudioDialogType, ReadAndSayTextType, AnswerSheetType

from graphql_relay.node.node import from_global_id

from graphene_file_upload.scalars import Upload

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

class CreateReadAndSayText(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        test = graphene.ID()
        number = graphene.Int()
    
    model = graphene.Field(ReadAndSayTextType)


    @classmethod
    def mutate(cls, root, info, text, test, number):
        testInstance = Test.objects.get(id=from_global_id(test)[1])
        print(testInstance)
        model = ReadAndSayText.objects.create(test=testInstance, content=text, 
            number=number, title="")
        return CreateReadAndSayText(model = model)

class UpdateReadAndSayText(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        task_id = graphene.ID()
        content = graphene.String()
        title = graphene.String()
    
    @classmethod
    def mutate(cls, root, info, task_id, content=None, title=None):
        taskInstance = ReadAndSayText.objects.get(id=from_global_id(task_id)[1])
        if content: taskInstance.content = content
        if title: taskInstance.title = title
        taskInstance.save()
        print(taskInstance.title)
        return UpdateReadAndSayText(ok=True)

class UpdateAudioDialog(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        file = Upload()
        title = graphene.String()
    
    model = graphene.Field(AudioDialogType)

    @classmethod
    def mutate(cls, root, info, id, file=None, title=None):
        model = AudioDialog.objects.get(id=from_global_id(id)[1])
        if file and not (file.name == "unnamed.PYC"): model.content = file
        if title: model.title = title
        model.save()
        print(model, model.title, AudioDialog.objects.get(id=from_global_id(id)[1]).title)
        return UpdateAudioDialog(model=model)

class CreateAudioDialog(graphene.Mutation):
    class Arguments:
        test_id = graphene.ID()
        file = Upload()
        title = graphene.String()
        number = graphene.Int()
    
    model = graphene.Field(AudioDialogType)

    @classmethod
    def mutate(cls, root, info, test_id, file, title, number):
        test = Test.objects.get(id=from_global_id(test_id)[1])
        model = AudioDialog.objects.create(test=test, content=file, title=title, number=number)
        return CreateAudioDialog(model=model)


class CreateAnswerSheet(graphene.Mutation):
    class Arguments:
        test_id = graphene.String()
        token = graphene.String()
    
    answerSheet = graphene.Field(AnswerSheetType)

    @classmethod
    def mutate(cls, root, info, test_id, token):
        
        model = AnswerSheet.objects.create(user=info.context.user, test=Test.objects.get(pk=from_global_id(test_id)[1]))
        return CreateAnswerSheet(answerSheet=model)


class CreateReadAndSayAnswer(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        task_id = graphene.ID()
        asnwer_sheet_id = graphene.ID()
        answer = Upload()
    

    @classmethod
    def mutate(cls, root, info, task_id, answer_sheet_id, answer):
        answerSheet = AnswerSheet.objects.get(id=from_global_id(answer_sheet_id)[1])
        task = ReadAndSayText.objects.get(id=from_global_id(answer_sheet_id)[1])

        AudioDialogAnswer.objects.create(answerSheet=answerSheet, task=task, content=answer)
        return CreateReadAndSayAnswer(ok=True)