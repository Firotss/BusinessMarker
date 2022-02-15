from django.urls import include, path
from .views import *

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('ajax/', AjaxView.as_view()),
    path('logout/', logout_view, name='logout'),
    path('delete/', delete, name='delete'),
]
