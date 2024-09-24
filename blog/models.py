from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=200
        )
    content = models.TextField(
        verbose_name='Content',
    )
    author = models.CharField(
        verbose_name='Author',
        max_length=100)
    
    created_at = models.DateTimeField(
        verbose_name='Date and time of creation',
        default=timezone.now,
                
    )

    show_home = models.BooleanField(
        'Show at home',
        default=False
    )

    def __str__(self):
        return self.title
    
    