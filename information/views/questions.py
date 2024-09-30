from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from information.models import Questions
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from information.decorators import user_can_delete
from django.contrib import messages


class QuestionsList(ListView):
      model = Questions
      template_name = 'general/questions.html'
      context_object_name = 'questions'

class QuestionsDetail(DetailView):
    model = Questions
    template_name = 'general/question_detail.html'
    context_object_name = 'question_detail'

    
@method_decorator(login_required, name='dispatch')
class QuestionsCreateView(CreateView):
      model = Questions
      fields = [
          'topic',
          'question',
          
          ]
      template_name = 'general/new_question.html'

      success_url = reverse_lazy('information:questionlist')

      def form_valid(self, form):
          messages.success(self.request, f'Question successfully created')
          form.instance.created_by = self.request.user
          return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class QuestionsUpdateView(UpdateView):
      model = Questions
      fields = [
          'topic',
          'question',
          ]
      template_name = 'general/update_question.html'
      success_url = reverse_lazy('information:questionlist')
      def form_valid(self, form):
          messages.success(self.request, f'Question successfully updated')
          form.instance.created_by = self.request.user
          return super().form_valid(form)

@method_decorator(user_can_delete, name='dispatch')
class QuestionsDeleteView(DeleteView):
      model = Questions
      success_url = reverse_lazy('information:questionlist')
      template_name = 'general/delete_question.html'
      def deleting(self):
          messages.success(self.request, f'Question successfully delete')
          return render (self.request, 'general/question_detail.html')

