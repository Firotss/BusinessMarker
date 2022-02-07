from django.urls import include, path
from .views import *
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('ajax/', AjaxView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete, name='delete'),
]
