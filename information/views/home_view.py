from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from django.contrib import messages

def home_view(request):
      # messages.success(request, 'Wellcome')
      return render(request, 'general/home.html')