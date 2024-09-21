from django.shortcuts import render
from courses.models import Course
from django.contrib.auth.decorators import login_required

@login_required
def courses_view(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'courses/courses.html', context)



    