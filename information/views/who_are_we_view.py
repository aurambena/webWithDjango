from django.shortcuts import render

def who_are_we_view(request):
      return render(request, 'who_are_we/who_are_we.html')