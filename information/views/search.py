from django.shortcuts import render
from information.forms import SearchForm
from courses.views import Course

# def search_view(request):
#         if request.GET:
#             search = request.GET['s']
#             courses = Course.objects.filter(title__icontains=search)

#             context = {
#                  'courses' : courses,
#             }
#             return render (request, 'general/search.html', context)
        
#         return render (request, 'general/search.html')

def search_view(request):
    if request.GET:
        form = SearchForm(request.GET)
        search = request.GET['s']
        print(form.f.cleaned_data)
        courses = Course.objects.filter(title__icontains=search)
        context ={
            'form':form,
            'courses':courses,
        }
        return render (request, 'general/search.html', context)
    else:
        form = SearchForm()
        context ={
            'form':form,
        }
        return render (request, 'general/search.html',context)

        
    
    
