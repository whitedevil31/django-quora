from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer
from django.views import generic
from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse
from .forms import answerPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
class answerPostView(LoginRequiredMixin,generic.CreateView):
    template_name='answers/post_answer.html'
    form_class=answerPostForm
    def get_success_url(self):
        return reverse('users:user-list')    
    def form_valid(self,form):
        temp=form.save(commit=False)
        temp.author=self.request.user
        temp.answered_on=datetime.now()
        temp.question_id=self.kwargs['pk']
        temp.save()
        return super().form_valid(form)
