from django.core.checks.messages import Error
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random

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
                username = ""
                password = ""
                email = None
                try:
                    username = request.POST['username']
                    password = request.POST['password']
                    email = request.POST['email']
                except:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/profile/')
                try: 
                    user = User.objects.create_user(username, email, password)
                    i = 6
                    code = ""
                    while i > 0:
                        code+=(str)(random.randint(0,9))
                        i-=1
                    send_mail(
                        'UR CODE:',
                        code,
                        '',
                        [email],
                        fail_silently=False,
                    )
                    print(code)
                    user.save()
                    return redirect('/profile/')
                except:
                    return render(request, 'login.html')   
                
        else:
            return redirect('/profile/')
                

