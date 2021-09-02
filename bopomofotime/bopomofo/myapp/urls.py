from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        path('', views.index),
#        path('<int:page>/', views.page_view),
        path('login/', auth_views.LoginView.as_view()),
        path('register/', views.register),
        path('logout/', views.logout_view),
]
