# Create your models here.
from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField



# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name='Course title',
        max_length=200
        )
    content = RichTextField(
        verbose_name='Course content',
    )
    call = models.URLField(
        verbose_name='call link',
        )
    
    created_at = models.DateTimeField(
        verbose_name='Date and time of creation',
        default=timezone.now
    )

    show_home = models.BooleanField(
        'Show at home',
        default=False
    )

    content_list = models.FileField(
        'listed content',
        upload_to='courses/list/',
        null=True,
        blank = True,
    )

    course_image = ImageField(
        verbose_name='cover',
        upload_to= 'courses/images/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
    
    