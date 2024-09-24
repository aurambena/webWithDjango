from django.shortcuts import render, redirect
from blog.forms import  PostModelForm
from blog.models import Post
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class NewsList(ListView):
    model = Post
    template_name = 'blog/blog_news_list.html'

class NewsDetail(DetailView):
    model = Post
    template_name = 'blog/blog_news_detail.html'
    context_object_name = 'blog_news_detail'
