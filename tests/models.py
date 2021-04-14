from django.db import models

from django.contrib.auth.models import User

import uuid

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Test(models.Model):
    name = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __len__(self):
        return len(self.readandsaytext_set.all()) + len(self.audiodialog_set.all())


class Task(models.Model):

    class Meta:
        abstract = True

    title = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(default=1)

    id = models.UUIDField(default=uuid.uuid4, editable=False, blank=True, primary_key=True)

    def stringify_practise(self) : pass


class WriteTask(Task): pass


class ReadAndSayText(Task):
    content = models.TextField()

    def vName(self) : return "ReadAndSayText"


class AudioDialog(Task):
    content = models.FileField()    

    def vName(self) : return "AudioDialog"

class AnswerSheet(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, on_delete=models.CASCADE, null=True)


class Answer(models.Model):

    class Meta:
        abstract = True

    answerSheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)


class ReadAndSayAnswer(Answer):
    task = models.ForeignKey(ReadAndSayText, on_delete=models.CASCADE)
    content = models.FileField(upload_to="audios")


class AudioDialogAnswer(Answer):
    task = models.ForeignKey(AudioDialog, on_delete=models.CASCADE)
    content = models.FileField(upload_to="audios")