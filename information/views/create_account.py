from django.shortcuts import render
from courses.models import Course
from information.forms import AccountForm
from information.models import Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



def account_view(request):
        if request.POST:
            form = AccountForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']

                user = User.objects.create_user(username, email, password1)
                if user:
                     user.first_name = first_name
                     user.last_name = last_name
                     user.save()

                context = {
                     'message': 'User successfully created'
                }
                return render (request, 'general/create_account.html', context)

                
            else:
                context = {
                  'form':form,
                  'error': True
                }
                return render (request, 'general/create_account.html', context)

           
        form = AccountForm()
        context={
              'form':form,
        }
        return render (request, 'general/create_account.html',context)