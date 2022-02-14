from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login_menu/login/', views.login_func),
    path('login_menu/register/', views.register),
    path('login_menu/', views.login_view, name='login'),
    path('phpmyadmin/', views.phpmyadmin),
    path('ref/<str:id>/', views.ref),
    path('handler404', views.error_404)
]