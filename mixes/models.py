from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class AudioPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    audio_file = CloudinaryField('audio')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    class Meta:
        db_table = 'hello_world_audiopost'
