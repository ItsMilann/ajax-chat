from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    admin_message = models.CharField(max_length=255, blank=True, null=True)
    client = models.CharField(max_length=255, default='Anonymous')
    client_message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.client