from django.urls import path

from .views import(
    blog_view,
    blog_detail,
)

app_name= 'blog'
urlpatterns = [
    path('blog/', blog_view, name='blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail')

]
