from django.urls import path

from .views import(
    blog_view,
    blog_detail,
    new_post_view,
    NewsList,
    NewsDetail,
)

app_name= 'blog'
urlpatterns = [
    path('blog/', blog_view, name='blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('blog/new_post/', new_post_view, name='new_post'),
    path('blog/news_list/', NewsList.as_view(), name='news_list'),
    path('blog/news_detail/<pk>/', NewsDetail.as_view(), name='news_detail'),


]
    