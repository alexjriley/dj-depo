from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import sys

class AudioPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # During tests we prefer a local FileField to avoid uploading test files to Cloudinary
    if 'test' in sys.argv:
        audio_file = models.FileField(upload_to='audio/')
    else:
        # Use resource_type='auto' so audio files (mp3, wav, etc.) are accepted
        audio_file = CloudinaryField('audio', resource_type='auto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    class Meta:
        db_table = 'hello_world_audiopost'
        app_label = 'mixes'
