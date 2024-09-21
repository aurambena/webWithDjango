from django.shortcuts import render
from courses.models import Course


def courses_detail(request, id):
    course = Course.objects.get(pk=id)
    context = {
        'course': course
    }
    return render(request, 'courses/courses_detail.html', context)
