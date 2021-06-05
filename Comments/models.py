from django.contrib.auth.models import User
from django.db import models

from Posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comment_post", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="comment_user", on_delete=models.CASCADE
    )
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.id
