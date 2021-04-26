from django.db import models

from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField

import uuid

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Test(models.Model):
    name = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def getTasks(self):
        return [*self.readandsaytext_set.all(), *self.audiodialog_set.all(), *self.themeselectionandsay_set.all()]

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


class ThemeSelectionAndSay(Task):
    content = ArrayField(models.TextField())

    def vName(self): return "ThemeSelectionAndSay"

class ReadAndSayText(Task):
    content = models.TextField(default="")

    def vName(self) : return "ReadAndSayText"


class AudioDialog(Task):
    content = models.FileField(blank=True)    

    def vName(self) : return "AudioDialog"

class AnswerSheet(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, on_delete=models.CASCADE, null=True)

    def getTasks(self):
        return sorted([*self.readandsayanswer_set.all(), 
            *self.audiodialoganswer_set.all(),
            *self.themeselectionandsayanswer_set.all()], key=lambda x : x.task.number)

    def __len__(self):
        return len(self.readandsayanswer_set.all()) + len(self.audiodialoganswer_set.all()) + len(self.themeselectionandsayanswer_set.all())


class Answer(models.Model):

    class Meta:
        abstract = True 
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    #uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True, primary_key=True)
    answerSheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)


class ReadAndSayAnswer(Answer):
    task = models.ForeignKey(ReadAndSayText, on_delete=models.CASCADE)
    content = models.FileField(upload_to="audios")

    def Type(self) : return "ReadAndSayAnswer"



class AudioDialogAnswer(Answer):
    task = models.ForeignKey(AudioDialog, on_delete=models.CASCADE)
    content = models.FileField(upload_to="audios")

    def Type(self) : return "AudioDialogAnswer"

class ThemeSelectionAndSayAnswer(Answer):
    task = models.ForeignKey(ThemeSelectionAndSay, on_delete=models.CASCADE)
    content = models.FileField(upload_to="audios")
    theme_selected = models.TextField()

    def Type(self) : return "ThemeSelecitonAndSayAnswer"