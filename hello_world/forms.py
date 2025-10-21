from django import forms
from .models import AudioPost

class MixUploadForm(forms.ModelForm):
    class Meta:
        model = Mix
        fields = ['title', 'description', 'audio_file']
