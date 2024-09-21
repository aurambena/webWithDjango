from django.shortcuts import render, redirect
from information.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def logout_view(request):
    logout(request)
    return redirect(reverse('information:home'))