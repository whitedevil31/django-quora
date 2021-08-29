from django.db import models
from django.contrib.auth.models import AbstractUser
# import uuid 
# class User(models.Model):
#     first_name=models.CharField(max_length=30,blank=True)
#     email=models.EmailField(blank=True)
#     bio=models.CharField(max_length=100,default="",blank=False)
#     id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     def __str__(self):
#         return self.first_name

class User(AbstractUser):
    pass