import graphene

import graphql_jwt

from .djangoTypes import TestType, ReadAndSayTextType, AudioDialogType, AudioDialogAnswerType, ReadAndSayAnswerType

from .models import Test, ReadAndSayText, AudioDialog

from .mutations import *

from graphene_django.filter import DjangoFilterConnectionField

from graphene import relay

from graphql_relay.node.node import from_global_id

class Query(graphene.ObjectType):
    
    testByUser = graphene.List(TestType, token=graphene.String())

    allTests = DjangoFilterConnectionField(TestType)


    testdetail = relay.Node.Field(TestType)
    get_read_and_say_text_type = graphene.Field(ReadAndSayTextType, id=graphene.String())
    get_audioDialog = graphene.Field(AudioDialogType, id=graphene.String())
    get_theme_selection_and_say = graphene.Field(ThemeSelectionAndSayType, id=graphene.ID())


    answerSheet = relay.Node.Field(AnswerSheetType)
    get_audio_dialog_answer = graphene.Field(AudioDialogAnswerType, id=graphene.ID())
    get_read_and_say_answer = graphene.Field(ReadAndSayAnswerType, id=graphene.ID())
    get_theme_selection_answer = graphene.Field(ThemeSelectionAndSayAnswerType, id=graphene.ID())


    def resolve_get_theme_selection_answer(self, info, id):
        return ThemeSelectionAndSayAnswer.objects.get(id=from_global_id(id)[1])

    def resolve_get_theme_selection_and_say(self, info, id):
        return ThemeSelectionAndSay.objects.get(id=from_global_id(id)[1])

    def resolve_get_audio_dialog_answer(self, info, id):
        return AudioDialogAnswer.objects.get(id=from_global_id(id)[1])
    

    def resolve_get_read_and_say_answer(self, info, id):
        return ReadAndSayAnswer.objects.get(id=from_global_id(id)[1])


    def resolve_testByUser(self, info, token):
        return Test.objects.filter(user=info.context.user)
    

    def resolve_get_read_and_say_text_type(self, info, id):
        taskId = from_global_id(id)[1]
        return ReadAndSayText.objects.get(id=taskId)
    

    def resolve_get_audioDialog(self, info, id):
        return AudioDialog.objects.get(id=from_global_id(id)[1])



class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    user_auth = RegisterUser.Field()

    create_test = CreateTest.Field()
    delete_test = DeleteTest.Field()

    create_listen_and_say_text = CreateReadAndSayText.Field()
    update_listen_and_say_text = UpdateReadAndSayText.Field()

    create_theme_selection_and_say = CreateThemeSelection.Field()
    update_theme_selection_and_say = UpdateThemeSelection.Field()

    create_audio_dialog = CreateAudioDialog.Field()
    update_audio_dialog = UpdateAudioDialog.Field()

    
    create_answer_sheet = CreateAnswerSheet.Field()
    create_read_and_say_answer = CreateReadAndSayAnswer.Field()
    create_audio_dialog_answer = CreateAnswerDialog.Field()
    create_theme_selection_and_say_answer = CreateThemeSelectionAnswer.Field()

    delete_task = DeleteTask.Field()
    rebase_task = RebaseTask.Field()
    create_blank_test = createBlankTemplateTest.Field()