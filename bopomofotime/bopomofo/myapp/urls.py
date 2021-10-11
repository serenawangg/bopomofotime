from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        path('', views.index),
#        path('<int:page>/', views.page_view),
        path('login/', auth_views.LoginView.as_view()),
        path('register/', views.register),
        path('logout/', views.logout_view),
        path('studypage/', views.studypage),
        path('mixandmatch/', views.mixandmatch),
        path('guesstheletter/', views.guesstheletter),
        path('traceit/', views.traceit),
        path('drawandcompare/', views.drawandcompare),
        path('drawandcompare2/', views.drawandcompare2),
]
