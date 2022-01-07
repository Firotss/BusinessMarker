from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete, name='delete'),
]
