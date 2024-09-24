from django.db import models
from django.utils import timezone


# Create your models here.
class Contact (models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=50
        )
    email = models.EmailField(
        verbose_name='email',
    )
    coment = models.TextField(
        verbose_name='coment'
    )
    created_at = models.DateTimeField(
        verbose_name='date and time',
        default=timezone.now,
    )
    contacted = models.BooleanField(
        verbose_name='¿Has been contacted?',
        default=False
    )

    def __str__(self):
        return self.name
    
class Questions(models.Model):
    topic = models.CharField(
        verbose_name='topic',
        max_length=50
        )
    
    question = models.CharField(
        verbose_name='question',
        max_length=200,
        )
    
    def __str__(self):
        return self.question