from django.shortcuts import render, redirect
from information.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login_view(request):
        if request.POST:
            form = LoginForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('information:home'))
                else:
                     context = {
                  'form':form,
                  'error': True,
                  'error_message':'Not valid user'
                }
                return render (request, 'general/login.html', context)
            else:
                context = {
                  'form':form,
                  'error': True
                }
                return render (request, 'general/login.html', context)

           
        form = LoginForm()
        context={
              'form':form,
        }
        return render (request, 'general/login.html',context)