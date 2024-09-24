from django.contrib import admin
from .models import Contact, Questions

# Register your models here.

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'coment', 'created_at', 'contacted')
    list_filter = ('contacted',)

@admin.register(Questions)
class ContactResource(admin.ModelAdmin):
    model = Questions
    list_display = ('topic', 'question', 'pk')
    
    
