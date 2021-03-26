from django.db import models

from django.contrib.auth.models import User

class Test(models.Model):
    name = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    theory = models.TextField()
    practise = models.TextField()


class AnswerSheet(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)


class Answer(models.Model):
    answerSheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    answer = models.TextField()
