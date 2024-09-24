from django.shortcuts import render, redirect
from blog.forms import  PostModelForm
from blog.models import Post
from django.urls import reverse

def new_post_view(request):
    if request.POST:
        form = PostModelForm(request.POST)
        if form.is_valid():
            new_post = Post.objects.create(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                author = form.cleaned_data['author'],
            )

            print('New Post Created')
            return redirect(reverse('blog:blog_detail', kwargs={'id': new_post.pk}))
    else:
        form = PostModelForm()
    
    context={
        'form': form,
    }
    return render(request, 'blog/new_post.html',context)

