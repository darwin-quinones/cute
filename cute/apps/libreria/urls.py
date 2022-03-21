from django.urls import path
from . import views

# el archivo de configuraciones
from django.conf import settings  
# config para mstrar l img
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.libreria, name='libreria'),
    path('index', views.index_libro, name='index_libro'),
    path('add_book', views.add_book, name='add_book'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)