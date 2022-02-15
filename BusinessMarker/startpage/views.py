from django.core.checks.messages import Error
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from .models import Ref_Links

class IndexView(TemplateView):
    template_name = 'index.html'

# def index(request):
#     return render(request, 'index.html')

def phpmyadmin(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    
def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            if User.objects.filter(username=username).exists() == False:
                i = 10
                code = ""
                while i > 0:
                    code+=(str)(random.randint(0,9))
                    i-=1
                
                try:
                    Ref_Links.objects.get(username=username).delete()
                except:
                    print()

                Ref_Links.objects.create(username=username, password=password, email=email, code=code)
                code = "https://www.businessmarker.ru/ref/"+username+"-"+code
                send_mail(
                    'Confirm ur email:',
                    code,
                    'tech-support@businessmarker.ru',
                    [email],
                    fail_silently=False,
                )
        return redirect('/login_menu/')
    else:
        return redirect('/profile/')

def login_func(request):
    if not request.user.is_authenticated: 
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('/profile/')
        return redirect('/login_menu/')
    else:
        return redirect('/profile/')

def login_view(request):
    loginForm = LoginForm()
    registerForm = RegisterForm()
    if not request.user.is_authenticated: 
        return render(request, 'login.html', {'login_form' : loginForm, 'register_form' : registerForm})  
    else:
        return redirect('/profile/')
                
def ref(request, id):
    id_list = id.split('-')
    if(Ref_Links.objects.filter(username=id_list[0])):
        ref_code = Ref_Links.objects.filter(username=id_list[0])
        if(ref_code[0].code == id_list[1]):
            user = User.objects.create_user(ref_code[0].username, ref_code[0].email, ref_code[0].password)
            basic_group = Group.objects.get(name='Free') 
            user.groups.add(basic_group)
            Ref_Links.objects.get(username=id_list[0]).delete()
            login(request, user)
    return redirect('/profile/')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def test_handler(request):
    return render(request, '404.html')