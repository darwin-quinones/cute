from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    password = request.POST['password']
    email = request.POST['email']
    # validacion del user
    try:
        user = User.objects.get(email=email)
        if user.password == password:
            return redirect('index')
        else:
            messages.success(request, 'Contraseña incorrecta')
            return redirect('home')
    except:
        messages.success(request, 'Usuario no registrado')
        return redirect('home')
def index(request):
    return render(request, 'user/index.html')

def logout_request(request):
    logout(request)
    messages.success(request, 'cerrado')
    return redirect('home')
