from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    receiver = models.ForeignKey(
        User, related_name="receiver", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.id
