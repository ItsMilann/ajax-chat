from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['client', 'client_message', 'admin_message']



admin.site.register(Message, MessageAdmin)