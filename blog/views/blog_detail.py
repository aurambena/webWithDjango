from django.shortcuts import render
from blog.models import Post

def blog_detail(request,id):
    posts = Post.objects.get(pk=id)
    context = {
        'post': posts
    }
    return render(request, 'blog/blog_detail.html', context)

