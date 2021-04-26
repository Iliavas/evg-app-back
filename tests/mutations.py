import graphene

from django.contrib.auth.models import User

from .models import Test, ReadAndSayText, AudioDialog, AnswerSheet, AudioDialogAnswer, ReadAndSayAnswer

from .djangoTypes import *

from graphql_relay.node.node import from_global_id

from graphene_file_upload.scalars import Upload

from .modelTaskDecoder import *

import graphql

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
        print(title, model.title, AudioDialog.objects.get(id=from_global_id(id)[1]).title)
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
        answer_sheet_id = graphene.ID()
        answer = Upload()
    

    @classmethod
    def mutate(cls, root, info, task_id, answer_sheet_id, answer):
        print(task_id, from_global_id(task_id))
        answerSheet = AnswerSheet.objects.get(id=from_global_id(answer_sheet_id)[1])
        task = ReadAndSayText.objects.get(id=from_global_id(task_id)[1])

        
        try:
            audioDialogLateObject = ReadAndSayAnswer.objects.get(task=task, answerSheet=answerSheet)
            audioDialogLateObject.delete()
        except TypeError:
            pass
        except:
            pass

        ReadAndSayAnswer.objects.create(answerSheet=answerSheet, task=task, content=answer)
        return CreateReadAndSayAnswer(ok=True)

class CreateAnswerDialog(graphene.Mutation):
    class Arguments:
        answer_sheet_id = graphene.ID()
        task_id = graphene.ID()
        
        answer = Upload()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, task_id, answer_sheet_id, answer):
        print(task_id, from_global_id(task_id))
        answerSheet = AnswerSheet.objects.get(id=from_global_id(answer_sheet_id)[1])
        task = AudioDialog.objects.get(id=from_global_id(task_id)[1])

        
        try:
            audioDialogLateObject = AudioDialogAnswer.objects.get(task=task, answerSheet=answerSheet)
            audioDialogLateObject.delete()
        except TypeError:
            pass
        except:
            pass
        print(answer)
        AudioDialogAnswer.objects.create(answerSheet=answerSheet, task=task, content=answer)
        return CreateReadAndSayAnswer(ok=True)


class CreateThemeSelection(graphene.Mutation):
    class Arguments:
        test_id = graphene.ID()
        number = graphene.Int()
    
    task = graphene.Field(ThemeSelectionAndSayType)

    @classmethod
    def mutate(cls, root, info, test_id, number):
        test = Test.objects.get(id=from_global_id(test_id)[1])

        task = ThemeSelectionAndSay.objects.create(content=[], title="", test=test, number=number)

        return CreateThemeSelection(task)

class ThemeSelectionInput(graphene.InputObjectType):
    content = graphene.Field(graphene.String)

class UpdateThemeSelection(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID()
        content = graphene.List(ThemeSelectionInput)
        title = graphene.String()
    
    ok = graphene.Boolean()
    
    @classmethod
    def mutate(cls, root, info, task_id, content=None, title=None):
        model = ThemeSelectionAndSay.objects.get(id=from_global_id(task_id)[1])

        if title: model.title = title
        if content: model.content = list(map(lambda x : x.content, content))
        model.save()

        return UpdateThemeSelection(ok=True)


class CreateThemeSelectionAnswer(graphene.Mutation):
    class Arguments:
        file = Upload()
        theme = graphene.String()
        task_id = graphene.ID()
        answer_sheet_id = graphene.ID()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, file, theme, task_id, answer_sheet_id):
        answer_sheet = AnswerSheet.objects.get(id=from_global_id(answer_sheet_id)[1])

        task = ThemeSelectionAndSay.objects.get(id=from_global_id(task_id)[1])

        try:
            answer = ThemeSelectionAndSayAnswer.objects.get(task=task, answerSheet=answer_sheet)
            answer.delete()
        except: pass
        answer = ThemeSelectionAndSayAnswer.objects.create(task=task, answerSheet=answer_sheet, 
            content=file, theme_selected=theme)
        print(answer)
        return CreateThemeSelectionAnswer(ok=True)


class DeleteTask(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID()
        test_id = graphene.ID()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, task_id, test_id):
        
        other_tasks = Test.objects.get(id=from_global_id(test_id)[1]).getTasks()
        decoded_id = from_global_id(task_id)[1]
        print(decoded_id, other_tasks)


        for test_task in other_tasks:
            if str(decoded_id) == str(test_task.id):
                test_task.delete()
                print(test_task)

        other_tasks = Test.objects.get(id=from_global_id(test_id)[1]).getTasks()
        other_tasks.sort(key=lambda x : x.number)

        for number, test_task in enumerate(other_tasks):
            test_task.number = number
            test_task.save()
            test_task.number
        
        for t in other_tasks:
            print(t.number)
        return DeleteTask(ok=True)


class RebaseTask(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID()
        test_id = graphene.ID()
        newType = graphene.String()
    

    ok = graphene.Boolean()

    answer = graphene.Field(TaskResponseType)

    @classmethod
    def mutate(cls, root, info, task_id, test_id, newType):
        test = Test.objects.get(id=from_global_id(test_id)[1])

        recoveredTaskId = from_global_id(task_id)[1]

        serialNumber = 0
        serialTitle = ""

        for i in test.getTasks():
            if str(recoveredTaskId) == str(i.id):
                print(i, i.number)
                serialNumber = i.number
                serialTitle = i.title
                i.delete()
        print(serialNumber, " asdf", test)
        newTask = TaskDecoder[newType].objects.create(test=test, number=serialNumber, title=i.title)

        return RebaseTask(ok=True, answer=newTask)


class createBlankTemplateTest(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        token = graphene.String()

    test = graphene.Field(TestType)


    @classmethod
    def mutate(cls, root, info, name, token):
        test = Test.objects.create(name = name, user=info.context.user)

        sampleTask = ReadAndSayText.objects.create(title="", test=test, number=1, content="")

        return createBlankTemplateTest(test=test)


class DeleteTest(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        Test.objects.get(id=from_global_id(id)[1]).delete()

        return DeleteTest(ok=True)