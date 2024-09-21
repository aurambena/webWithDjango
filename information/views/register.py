from django.shortcuts import render
from courses.models import Course
from information.forms import RegisterForm
from django.core.mail import send_mail
from information.models import Contact

# def register_view(request):
#         if request.POST:
#             name = request.POST['name']
#             email = request.POST['email']
#             coment = request.POST['coment']

#             context = {
#                   'name':name,
#                   'email':email,
#                   'coment':coment,
#             }
#             return render (request, 'general/register.html', context)
        
#         return render (request, 'general/register.html')

def register_view(request):
        if request.POST:
            form = RegisterForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                coment = form.cleaned_data['coment']
                print(f'name {name}, email {email}, coment {coment}')
                message_content = f'{name} with email {email} has written {coment}'
                Contact.objects.create(
                     name = name,
                     email = email,
                     coment = coment,
                )
                #from gmail
                success = send_mail(
                     'Register form',
                     message_content,
                     'aurairdrops@gmail.com',
                     ['aura_berdugo@hotmail.com'],
                     fail_silently=False,
                )
                #from dominio
                # success = send_mail(
                #      'Register form',
                #      message_content,
                #      'info@laveladaconquer.com',
                #      ['aurairdrops@gmail.com'],
                #      fail_silently=False,
                # )
                context = {
                      'form':form,
                      'success': success
                }
                return render (request, 'general/register.html', context)
            else:
                context = {
                    'form': form,
                }
                return render (request, 'general/register.html', context)

        form = RegisterForm()
        context={
              'form':form,
        }
        return render (request, 'general/register.html',context)