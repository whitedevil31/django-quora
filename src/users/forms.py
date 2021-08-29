from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

User=get_user_model()
class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email')



class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username'),
        field_classes={'username':UsernameField}