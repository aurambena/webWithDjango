from django.contrib import admin

# Register your models here.
from .models import Course

# from .models import Post

@admin.register(Course)

class PostResource(admin.ModelAdmin):
    
    model = Course
    list_display = ('title', 'content', 'call', 'created_at')