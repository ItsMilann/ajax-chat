from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender_text = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')

    def __str__(self):
        return '{}'.format(self.sender.username)