from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        path('', views.index),
        path('about/', views.about),
        path('login/', auth_views.LoginView.as_view()),
        path('register/', views.register),
        path('logout/', views.logout_view),
        path('studypage/', views.studypage),
        path('mixandmatch/', views.mixandmatch),
        path('guesstheletter/', views.guesstheletter),
        path('memorizeandtrace/', views.memorizeandtrace),
        path('drawandcompare/', views.drawandcompare2),
]
