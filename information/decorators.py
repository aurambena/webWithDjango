from information.models import Questions
from django.http import Http404
from django.core.exceptions import PermissionDenied

def user_can_delete(function):
    def wrap(request, *args, **kwargs):
        try:
            question = Questions.objects.get(pk=kwargs['pk'])
        except Questions.DoesNotExist:
            raise Http404
        
        if request.user == question.created_by:
            return function(request,*args, **kwargs)
        
        raise PermissionDenied
    
    return wrap