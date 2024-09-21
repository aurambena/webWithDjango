from django.shortcuts import render
from blog.models import Post

def blog_view(request):
    posts = Post.objects.all()
    context = {
        'post': posts
    }
    return render(request, 'blog/blog.html', context)

