from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user


def home(request):
    return render(request, 'home.html')


def privacy_policy(request):
    return render(request, 'privacy.html')


def login(request):
    return render(request, 'authentication/login.html')


def logout(request):
    logout_user(request)
    return redirect('core:home')
