from django.shortcuts import render

from django.http import HttpResponse, Http404 

from .models import AudioDialog

from graphql_relay.node.node import from_global_id

import os

def audioDialogAudioDownload(request, id): 
    audio = AudioDialog.objects.get(id=from_global_id(id)[1]).content.path
    audio = "C:/Users/Ilia/Documents/evgenapp/evg-app-back/fuck/c.wav"
    print(audio)
    with open(audio, "rb") as file:
        try:
            response = HttpResponse(file)  
            response["content_type"] = "audio/mpeg"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(audio)
            return response
        except Exception as e:
            print(e)
            raise Http404