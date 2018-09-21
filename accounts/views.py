# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect


# Create your views here.
from django.contrib import auth
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect(reverse('home', args=[]))
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm()})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'])
            return redirect(reverse('auth:login', args=[]))
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegistrationForm()})


def logout(request):
    auth_logout(request)
    return redirect(reverse('home', args=[]))
        
            
            
