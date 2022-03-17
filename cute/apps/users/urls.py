from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout_request, name='logout'),
]