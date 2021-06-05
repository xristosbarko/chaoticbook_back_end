from django.contrib.auth.models import User
from django.db import models


class Follow(models.Model):
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE
    )
    pending = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("following", "follower"),)

    def __str__(self):
        return "%s %s" % (self.following, self.follower)
