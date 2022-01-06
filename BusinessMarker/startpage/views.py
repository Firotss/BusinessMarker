from django.core.checks.messages import Error
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from .models import Ref_Links

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
                    if User.objects.filter(username=username).exists() == False:
                        i = 10
                        code = ""
                        while i > 0:
                            code+=(str)(random.randint(0,9))
                            i-=1
                        Ref_Links.objects.create(username=username, password=password, email=email, code=code)
                        code = "http://localhost:8000/ref/"+username+"-"+code
                        send_mail(
                            'CLICK LINK:',
                            code,
                            '',
                            [email],
                            fail_silently=False,
                        )
                except:
                    print('=>login')
                return render(request, 'login.html')  
        else:
            return redirect('/profile/')
                
def ref(request, id):
    id_list = id.split('-')
    try:
        if(Ref_Links.objects.filter(username=id_list[0])):
            ref_code = Ref_Links.objects.filter(username=id_list[0])
            if(ref_code[0].code == id_list[1]):
                user = User.objects.create_user(ref_code[0].username, ref_code[0].email, ref_code[0].password)
                Ref_Links.objects.get(username=id_list[0]).delete()
                login(request, user)
        return redirect('/profile/')
    except:
        return redirect('/')
    

def delete(request):
    u = User.objects.get(username = request.user.username).delete()
    return redirect("/")