from django.urls import path
from django.urls import re_path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('validar_email', views.validar_email, name='validar_email'),
]