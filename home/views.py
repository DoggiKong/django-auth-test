from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return HttpResponse('Test API at /api')

def sign_in(request):
    if not request.user.is_authenticated:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return HttpResponse(f'Welcome, {username}')
        else:
            return render(request, 'home/sign_in.html')
    else:
        return HttpResponse('You are already logged in')

def sign_out(request):
    logout(request)
    return HttpResponse('You have been logged out')

def secret(request):
    if request.user.is_authenticated:
        return HttpResponse('You are allowed to see this secret')
    else:
        return HttpResponse('Go away')

def ajax(request):
    return render(request, 'home/ajax1.html')
