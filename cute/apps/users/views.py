from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import connection
from django.http import JsonResponse
import json
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
                request.session['id'] = user.id
                request.session['username'] = user.username
                request.session['email'] = user.email
                messages.success(request, f'{user.username} Logeado exitosamente')
                return redirect('index')
            else:
                messages.error(request, 'Contraseña incorrecta')
                return redirect('home')
        except Exception as e:
            messages.info(request, 'Usuario no registrado')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        # strip elimina espacios en blancos
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        #comprobacion si usuario existe
        try:
            user_exist = User.objects.get(email=email)
            if user_exist:
                messages.error(request, 'Email already registered')
                return redirect('home')
        except:
            # se registra
            user = User(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('home')
     
    return redirect('home')
    
def index(request):
    try:
        if request.session['id']:
            return render(request, 'user/index.html')
    except:
        return redirect('home')

def logout_request(request):

    try:
        del request.session['id']
        logout(request)
        messages.success(request, 'Saliste exitosamente')
        return redirect('home')
    except KeyError:
        pass
    return redirect('home')
    
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['email'])
            user.password = data['new_password']
            user.save()
            return JsonResponse({'status': True})
        except:
            pass
    return JsonResponse({'status': True})

def validar_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['email'])
            return JsonResponse({'data':user.id })
        except:
            pass
    return JsonResponse({'data': 'no_existe'})
    