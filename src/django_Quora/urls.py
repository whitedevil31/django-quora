"""django_Quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from users.views import signupView
#login view importing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('questions/',include('questions.urls')),
    path('answers/',include('answers.urls')),
    path('',LoginView.as_view(),name='login'),
    #base url to login
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',signupView.as_view(),name='signup')
]
