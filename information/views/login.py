from django.shortcuts import render, redirect
from information.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib import messages

class AALoginView(LoginView):
     
    template_name = 'general/login.html'
    form_class = LoginForm
    success_url = '/home/'

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'You are successfully logged in {user}')
        LoginView(self.request, form.get_user())
        return super().form_valid(form)
   

