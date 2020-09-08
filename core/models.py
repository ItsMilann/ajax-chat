from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
USER_JON = User.objects.all()[1]

class Message(models.Model):
    sender_text = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', default=1)

    def __str__(self):
        return '{}'.format(self.sender.username)