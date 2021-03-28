from django.db import models

from django.contrib.auth.models import User

class Test(models.Model):
    name = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):

    class Meta:
        abstract = True

    theory = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    

    def stringify_practise(self) : pass


class WriteTask(Task): pass


class AnswerSheet(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, on_delete=models.CASCADE, null=True)


class Answer(models.Model):

    class Meta:
        abstract = True

    answerSheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    taskNumber = models.IntegerField()


class LongWriteAnswer(Answer):
    answer = models.TextField()