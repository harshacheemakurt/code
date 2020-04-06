from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
urlpatterns = [
    path('', views.home),
    path('index/',views.index1, name = 'index1'),
    path('answers/', views.index1, name= 'answer'),
    path('login/', views.login,name= 'login'),
    path('register/', views.register,name= 'register'),


]
