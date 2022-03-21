from django.shortcuts import render, redirect
from .models import Libro

# Create your views here.
def libreria(request):
    return render(request, 'paginas/inicio.html')

def index_libro(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def add_book(request):
    return render(request, 'libros/crear.html')
