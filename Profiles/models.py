from django.db import models
from django.contrib.auth.models import User

CHOICES = (
	('Α', 'Άντρας'),
	('Γ', 'Γυναίκα')
)

class Profile(models.Model):
	def url(self, picture):
		return 'users/%s/profile_pictures/%s' % (self.user.id, picture)

	user = models.OneToOneField(User, related_name="profile_user", on_delete=models.CASCADE)
	birth_date = models.DateField()
	gender = models.CharField(max_length=1, choices=CHOICES)
	profile_picture = models.ImageField(upload_to=url, default='default/default.png')
	bio = models.TextField(blank=True)

	def __str__(self):
		return '%s' % self.user.username