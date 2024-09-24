from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from information.models import Questions
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class QuestionsList(ListView):
      model = Questions
      template_name = 'general/questions.html'
      context_object_name = 'questions'

class QuestionsDetail(DetailView):
    model = Questions
    template_name = 'general/question_detail.html'
    context_object_name = 'question_detail'

class QuestionsCreateView(CreateView):
      model = Questions
      fields = [
          'topic',
          'question',
          ]
      template_name = 'general/new_question.html'
      success_url = reverse_lazy('information:questionlist')

class QuestionsUpdateView(UpdateView):
      model = Questions
      fields = [
          'topic',
          'question',
          ]
      template_name = 'general/update_question.html'
      success_url = reverse_lazy('information:questionlist')

class QuestionsDeleteView(DeleteView):
      model = Questions
      success_url = reverse_lazy('information:questionlist')
      template_name = 'general/delete_question.html'
