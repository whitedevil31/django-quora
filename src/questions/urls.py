
from django.urls import path
from .views import questionPostView,allQuestionsView,myQuestionsView
app_name='questions'

urlpatterns = [
    path('',questionPostView.as_view(),name='question-post'),
    path('all/',allQuestionsView.as_view(),name='question-all'),
    path('me/',myQuestionsView.as_view(),name='question-me'),

]
