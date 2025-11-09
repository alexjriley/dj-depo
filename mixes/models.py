from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import sys

"""
This module contains the `AudioPost` model, which was originally defined in the `hello_world` app.

The model was moved to the `mixes` app to better align with the application's structure and functionality.

Despite the move, the database table name remains `hello_world_audiopost` to maintain compatibility with existing data.

This change does not affect the functionality of the application, as Django seamlessly handles the mapping between the model and the database table.
"""

class AudioPost(models.Model):
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
        return f"{self.title} by {self.user.username}"

    class Meta:
        db_table = 'hello_world_audiopost'
        app_label = 'mixes'
