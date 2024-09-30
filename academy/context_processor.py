from django.conf import settings

def get_key(request):
    test_key = settings.KEY
    return{
        'KEY':test_key,
    }