from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AudioPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.


def signup(request):
    """
    Handle user signup by displaying and processing the user registration form.
    If the form is valid, create a new user, log them in, and redirect to 'home'.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class AudioPostForm(forms.ModelForm):
    class Meta:
        model = AudioPost
        fields = ['title', 'audio_file']
    """
    Form for creating and updating AudioPost instances.
    """
@login_required
def upload_audio(request):
    """
    Handle audio file uploads by authenticated users.

    Displays a form for uploading audio files and processes the form submission.
    On successful upload, associates the audio post with the current user and redirects to 'home'.
    """
    if request.method == 'POST':
        form = AudioPostForm(request.POST, request.FILES)
        if form.is_valid():
            audio_post = form.save(commit=False)
            audio_post.user = request.user
            audio_post.save()
            messages.success(request, 'Your mix was uploaded successfully!')
            return redirect('home')
    else:
        messages.error(request, 'There was a problem uploading your mix.')
        form = AudioPostForm()
    return render(request, 'mixes/upload_audio.html', {'form': form})

# Home page view for Mixes app
def home_page_view(request):
    posts = AudioPost.objects.order_by('-created_at')
    return render(request, 'mixes/home.html', {'posts': posts})