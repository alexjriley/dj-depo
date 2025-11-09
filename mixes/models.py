from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import sys

class AudioPost(models.Model):
    """Django model that represents an audio post in the application"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Avoid uploading test files to Cloudinary
    if 'test' in sys.argv:
        audio_file = models.FileField(upload_to='audio/')
    else:
        # Accept audio files and store timestamp
        audio_file = CloudinaryField('audio', resource_type='auto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = getattr(self.user, 'username', str(self.user))
        return f"{self.title} by {username}"

    class Meta:
        """Ensures that the database table name remains consistent (hello_world_audiopost)"""
        db_table = 'hello_world_audiopost'
        app_label = 'mixes'
