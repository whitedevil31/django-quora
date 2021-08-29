
from django.urls import path
from .views import answerPostView
app_name='answers'

urlpatterns = [
    path('<int:pk>/',answerPostView.as_view(),name='answer-post'),
  

]
