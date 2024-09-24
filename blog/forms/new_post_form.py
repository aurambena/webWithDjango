from django import forms
from django.utils import timezone
from django.forms import ModelForm
from blog.models import Post


# class NewPost(forms.Form):
    
#     title = forms.CharField(
#         max_length=200,
#         label='title',
#         )
#     content = forms.CharField(
#         max_length=1000, 
#         label='coment',
#         widget=forms.Textarea,
#         )
#     author = forms.CharField(
#         max_length=100,
#         label='author',
#         )
    
#     created_at = forms.DateField(
#         widget=forms.SelectDateWidget,
#         )

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'created_at']
   
