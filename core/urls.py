from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
