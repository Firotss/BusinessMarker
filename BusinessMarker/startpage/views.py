from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
def index(request):
    return render(request, 'index.html')

def phpmyadmin(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html')
    else:
        return redirect("/login")

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
        if request.user.is_authenticated is False: 
                user = None
                try:
                    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                    user.save()
                except:
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                finally:
                    if user is not None:
                        login(request, user)
                        return redirect('/profile/')
                    return render(request, 'login.html')
        else:
            return redirect('/profile/')
                

       
