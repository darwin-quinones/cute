from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
         # validacion del user
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                messages.success(request, 'Logeado exitosamente')
                return redirect('index')
            else:
                messages.success(request, 'Contraseña incorrecta')
                return redirect('home')
        except Exception as e:
            messages.success(request, 'Usuario no registrado')
    return redirect('home')

    
def index(request):
    return render(request, 'user/index.html')

def logout_request(request):
    logout(request)
    messages.success(request, 'Saliste exitosamente')
    return redirect('home')
