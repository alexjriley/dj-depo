from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AudioPost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	audio_file = models.FileField(upload_to='audio/')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} by {self.user.username}"
