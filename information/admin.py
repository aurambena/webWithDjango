from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'coment', 'created_at', 'contacted')
    list_filter = ('contacted',)
    
