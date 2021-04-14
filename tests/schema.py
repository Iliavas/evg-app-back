import graphene

import graphql_jwt

from .djangoTypes import TestType, ReadAndSayTextType, AudioDialogType

from .models import Test, ReadAndSayText, AudioDialog

from .mutations import RegisterUser, CreateTest, CreateReadAndSayText, UpdateReadAndSayText, UpdateAudioDialog, CreateAudioDialog, CreateAnswerSheet

from graphene_django.filter import DjangoFilterConnectionField

from graphene import relay

from graphql_relay.node.node import from_global_id

class Query(graphene.ObjectType):
    
    testByUser = graphene.List(TestType, token=graphene.String())

    allTests = DjangoFilterConnectionField(TestType)

    testdetail = relay.Node.Field(TestType)
    get_read_and_say_text_type = graphene.Field(ReadAndSayTextType, id=graphene.String())
    get_audioDialog = graphene.Field(AudioDialogType, id=graphene.String())

    def resolve_testByUser(self, info, token):
        print(info.context.user)
        return Test.objects.filter(user=info.context.user)
    

    def resolve_get_read_and_say_text_type(self, info, id):
        taskId = from_global_id(id)[1]
        return ReadAndSayText.objects.get(id=taskId)
    

    def resolve_get_audioDialog(self, info, id):
        return AudioDialog(id=from_global_id(id)[1])



class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    user_auth = RegisterUser.Field()
    create_test = CreateTest.Field()
    create_listen_and_say_text = CreateReadAndSayText.Field()
    update_listen_and_say_text = UpdateReadAndSayText.Field()
    create_audio_dialog = CreateAudioDialog.Field()
    update_audio_dialog = UpdateAudioDialog.Field()
    create_answer_sheet = CreateAnswerSheet.Field()