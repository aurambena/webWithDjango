# Generated by Django 5.1.1 on 2024-09-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0007_contact_contacted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='topic')),
                ('question', models.CharField(max_length=200, verbose_name='cuestion')),
            ],
        ),
    ]
