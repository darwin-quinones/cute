from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user/home.html')

def index(request):
    return render(request, 'user/index.html')
