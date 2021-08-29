from django.urls import path
from .views import userCreateView,userListView,userDetailView,userUpdateView,userDeleteView,signupView
app_name='users'

urlpatterns = [
    path('',userListView.as_view(),name='user-list'),
    path('<int:pk>/', userDetailView.as_view(),name='user-detail'),
    path('create/', userCreateView.as_view(),name='user-create'),
    path('<int:pk>/update', userUpdateView.as_view(),name='user-update'),
    path('<int:pk>/delete', userDeleteView.as_view(),name='user-delete'),

]
