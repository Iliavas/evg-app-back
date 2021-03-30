from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    Users = models.ManyToManyField(User)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Mark(models.Model):
    mark = models.CharField(max_length=1)
    descryption = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    def __str__(self):
        return self.mark
    class Meta:
        ordering = ('mark',)