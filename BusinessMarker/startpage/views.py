from pickle import NONE
from django.core.checks.messages import Error
from django.http import HttpResponse, HttpResponseBadRequest, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib.auth.models import Group
from django.views.generic import TemplateView

from profilepage.utils.mixins import Permissions
from .forms import LoginForm, RegisterForm
from .models import Ref_Links
from .utils.mixins import Send

class IndexView(Send):
    template_name = 'index.html'

def phpmyadmin(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    
class LoginView(Permissions):
    def get(self, request, *args, **kwargs):
        loginForm = LoginForm(request.POST)
        registerForm = RegisterForm(request.POST)
        return render(request, "login.html", {'login_form' : loginForm, 'register_form' : registerForm})

    def post(self, request, *args, **kwargs):
        loginForm = LoginForm(request.POST)
        registerForm = RegisterForm(request.POST)
        if request.POST['action'] == "login":
            if loginForm.is_valid():
                user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/profile/')
                loginForm.add_error(None, 'LOGIN ERROR')
            else:
                loginForm.add_error(None, 'CAPTCHA ERROR')
        else:
            if registerForm.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                if User.objects.filter(username=username).exists() == False:
                    i = 10
                    code = ""
                    while i > 0:
                        code+=(str)(random.randint(0,9))
                        i-=1
                    
                    if Ref_Links.objects.filter(username=username).exists() == True:
                        Ref_Links.objects.get(username=username).delete()

                    Ref_Links.objects.create(username=username, password=password, email=email, code=code)
                    code = "https://www.businessmarker.ru/ref/"+username+"-"+code
                    if send_mail(
                        'Confirm ur email:',
                        code,
                        'tech-support@businessmarker.ru',
                        [email],
                        fail_silently=False):
                        registerForm.add_error(None, 'CONFIRM EMAIL')
            else:
                registerForm.add_error(None, 'REGISTER ERROR')
                
        return render(request, "login.html", {'login_form' : loginForm, 'register_form' : registerForm})

def ref(request, id):
    id_list = id.split('-')
    if User.objects.filter(username=id_list[0]).exists() == False:
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