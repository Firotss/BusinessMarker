from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/check', views.login_check, name='login_check'),
    path('login/reg', views.registration, name='registration'),
    path('login/logout', views.logout_view, name='logout'),
    path('login/', views.loginn, name='login'),
    path('phpmyadmin/', views.phpmyadmin),
]