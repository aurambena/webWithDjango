from django.shortcuts import render
from courses.models import Course
from blog.models import Post

def home_view(request):
      context={
            'course': Course.objects.filter(show_home = True),
            'post':Post.objects.filter(show_home = True),
      }
      return render(request, 'general/home.html',context)