from django.urls import path

from .views import(
    courses_view,
    courses_detail,
    
)

app_name= 'courses'
urlpatterns = [
    path('courses/', courses_view, name='courses'),
    path('courses/<int:id>/', courses_detail, name='courses_detail'),   

]
