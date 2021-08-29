from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.views import generic
from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse
from .forms import questionPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
class questionPostView(LoginRequiredMixin,generic.CreateView):
    template_name='questions/post_question.html'
    form_class=questionPostForm
    def get_success_url(self):
        return reverse('users:user-list')    
    def form_valid(self,form):
        temp=form.save(commit=False)
        temp.author=self.request.user
        temp.created=datetime.now()
        temp.save()
        return super().form_valid(form)

class allQuestionsView(LoginRequiredMixin,generic.ListView):
    template_name='questions/all_questions.html'
    queryset=Question.objects.all()
    context_object_name='questions'


class myQuestionsView(LoginRequiredMixin,generic.ListView):
    template_name='questions/my_questions.html'
    def get_queryset(self):
        author = self.request.user
        return Question.objects.filter(author=author)
    context_object_name='questions'