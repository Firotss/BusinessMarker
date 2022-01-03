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
        return HttpResponse(request.user.is_authenticated)
    
def login_view(request):
    if request.user.is_authenticated is False:  
        return render(request, 'login.html')
    else:
        return redirect("/profile/")

def login_check(request):
    if request.user.is_authenticated is False:  
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        return redirect("/login/")
    else:
        return redirect("/profile/")

def registration(request):
    if request.user.is_authenticated is False:  
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            login(request, user)
            return redirect("/profile/")
        except:
            return redirect('/login/')
    else:
        return redirect("/profile/")

        
def logout_view(request):
    logout(request)
    return redirect('/')

