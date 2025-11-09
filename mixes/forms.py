from django import forms
from .models import AudioPost

class MixUploadForm(forms.ModelForm):
    """A form for users to upload information"""
    class Meta:
        """Defines the form metadata"""
        model = AudioPost
        fields = ['title', 'description', 'audio_file']
