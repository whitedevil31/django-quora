
from django.db import models
from django.conf import settings
from questions.models import Question

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,default=1)
    answer= models.CharField(max_length=1000)
    answered_on=models.DateTimeField()
    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.answer
