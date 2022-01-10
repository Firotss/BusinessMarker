from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'baseProfile.html')
    else:
        return redirect("/login_menu/")

def logout_view(request):
    logout(request)
    return redirect('/')


def delete(request):
    User.objects.get(username = request.user.username).delete()
    return redirect("/")
