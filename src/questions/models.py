from django.db import models
from django.conf import settings

class Question(models.Model):
    question=models.CharField(max_length=200)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    created=models.DateTimeField()
    def __str__(self):
        return self.question
