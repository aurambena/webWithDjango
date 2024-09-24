from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class TestingView(View):
    def get(self, request, *arg, **kwargs):
        return HttpResponse('Hello World!')
    
class TestingTemplateView(TemplateView):
    template_name = 'general/TestingTemplateView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Testing Classy Class-Based Views'
        return context
    
# class TestingTemplateView2(TestingTemplateView):
#     template_name = 'general/TestingTemplateView.html'
