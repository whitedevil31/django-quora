from django import forms
from .models import Answer



class answerPostForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=('answer'),
