from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    
    def __str__(self):
        return self.question
    
class CreateAccount(models.Model):
    username = models.CharField(
        verbose_name='username',
        max_length=50
        )
    
    first_name = models.CharField(
        verbose_name='firstname',
        max_length=50
        )
    
    last_name = models.CharField(
        verbose_name='lastname',
        max_length=50
        )
    
    email = models.EmailField(
        verbose_name='email',
    )

    password1 = models.CharField(
        verbose_name='password1',
        max_length=15,
    )

    password2 = models.CharField(
        verbose_name='password1',
        max_length=15,
    )  
    
    def __str__(self):
        return self.username
    
