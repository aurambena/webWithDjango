# Generated by Django 5.1.1 on 2024-09-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=200, verbose_name='question'),
        ),
    ]
