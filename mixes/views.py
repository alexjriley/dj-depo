from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AudioPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseForbidden


def signup(request):
    """
    Handle user signup by displaying and processing the user registration form.
    If the form is valid, create a new user, log them in, and redirect to
    'home'.
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
        fields = ['title', 'description', 'audio_file']

    def clean_audio_file(self):
        audio_file = self.cleaned_data.get('audio_file')
        if audio_file:
            # Check if the file is a CloudinaryResource object
            if hasattr(audio_file, 'public_id'):
                # Skip validation for already uploaded files
                return audio_file

            # Validate the file extension using the original file name
            if not audio_file._name.lower().endswith('.mp3'):
                raise forms.ValidationError('Only MP3 files are allowed.')
        return audio_file


@login_required
def upload_audio(request):
    """
    Handle audio file uploads by authenticated users.

    Displays a form for uploading audio files and processes the form
    submission.

    On successful upload, associates the audio post with the current user and
    redirects to 'home'.
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
            # Form was submitted but invalid — show an error and re-render
            messages.error(request,
                           'There was a problem. Please try again.')
    else:
        # GET request — display a blank form without error messages
        form = AudioPostForm()
    return render(request, 'mixes/upload_audio.html', {'form': form})

# Home page view for Mixes app


def home_page_view(request):
    posts = getattr(AudioPost, 'objects').order_by('-created_at')
    # pylint: disable=no-member
    return render(request, 'mixes/home.html', {'posts': posts})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(AudioPost, pk=pk)

    # Only allow the user who created the post to delete it
    if post.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Your mix was deleted successfully!')
        return redirect('home')  # change 'home' to your desired redirect name

    return render(request, 'mixes/post_confirm_delete.html', {'post': post})


@login_required
def edit_audio_post(request, pk):
    post = get_object_or_404(AudioPost, pk=pk, user=request.user)
    # Ensure only the user's post is fetched

    form = AudioPostForm(
        request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your mix was updated successfully!')
        return redirect('home')
        # Ensure redirect after successful form submission

    # Debugging output
    print("Post object (ID):", post.id)
    print("Post object (Title):", post.title)
    print("Post object (Description):", post.description)
    print("Form initial data:", form.initial)

    return render(request, 'mixes/edit_audio_post.html', {
     'form': form, 'post': post})
