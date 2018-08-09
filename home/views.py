from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'home/index.html')

def secret(request):
    if request.user.is_authenticated:
        return render(request, 'home/secret.html', {'secret': 'You can see this secret'})
    else:
        return render(request, 'home/secret.html', {'secret': 'Go away'})

def ajax(request):
    return render(request, 'home/ajax.html')
