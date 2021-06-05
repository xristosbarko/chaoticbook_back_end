from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    def url(self, picture):
        return "users/%s/pictures/%s" % (self.user.id, picture)

    user = models.ForeignKey(
        User, related_name="post_user", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=60, blank=True)
    picture = models.ImageField(upload_to=url)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.id
