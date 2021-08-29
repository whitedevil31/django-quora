from django import forms
from .models import Question



class questionPostForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('question'),
