from django.urls import include, path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login_menu/login/', login_func),
    path('login_menu/register/', register),
    path('login_menu/', LoginView.as_view(), name='login'),
    path('phpmyadmin/', phpmyadmin),
    path('ref/<str:id>/', ref),
    path('404/', test_handler),
]