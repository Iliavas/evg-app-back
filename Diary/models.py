from django.db import models
from django.contrib.auth.models import User

class Mark(models.Model):
    mark = models.IntegerField()
    lesson = models.CharField(max_length=20)
    descryption = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.mark
    class Meta:
        ordering = ('mark',)