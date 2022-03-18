from django.shortcuts import render

# Create your views here.
def libreria(request):
    return render(request, 'paginas/inicio.html')

def index_libro(request):
    return render(request, 'libros/index.html')
