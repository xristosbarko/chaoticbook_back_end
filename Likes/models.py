from django.contrib.auth.models import User
from django.db import models

from Posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(
        Post, related_name="like_post", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="like_user", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("post", "user"),)

    def __str__(self):
        return "%s" % self.id
