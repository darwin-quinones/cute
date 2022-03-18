from django.urls import path
from . import views
urlpatterns = [
    path('', views.libreria, name='libreria'),
    path('index', views.index_libro, name='index_libro'),
]