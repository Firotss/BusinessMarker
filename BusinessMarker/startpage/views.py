from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def index(request):
    return render(request, 'index.html')

def phpmyadmin(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html')
    else:
        return render(request, 'login.html')
    
def login_view(request):
    if request.user.is_authenticated:
        return profile(request)
    else:     
        return render(request, 'login.html')

def login_check(request):
    if request.user.is_authenticated:
        return profile(request)
    else:     
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'user_profile.html')
        else:
            return render(request, 'login.html')
    

def registration(request):
    if request.user.is_authenticated:
        return profile(request)
    else:     
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, 'user_profile.html')
        except:
            return render(request, 'login.html')

        
def logout_view(request):
    logout(request)
    return render(request, 'index.html')