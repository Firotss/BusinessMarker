from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/logout', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('phpmyadmin/', views.phpmyadmin),
]