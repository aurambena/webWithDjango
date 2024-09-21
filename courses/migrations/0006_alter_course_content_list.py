# Generated by Django 5.1.1 on 2024-09-11 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_content_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content_list',
            field=models.FileField(blank=True, null=True, upload_to='courses/list/', verbose_name='listed content'),
        ),
    ]
