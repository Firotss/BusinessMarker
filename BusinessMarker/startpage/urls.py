from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/logout', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/check', views.login_check, name='login_check'),
    path('login/reg', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('phpmyadmin/', views.phpmyadmin),
]