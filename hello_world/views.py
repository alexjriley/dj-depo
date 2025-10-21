from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AudioPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def home_page_view(request):  
    posts = AudioPost.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
def home_page_view(request):
    posts = AudioPost.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

class AudioPostForm(forms.ModelForm):
    class Meta:
        model = AudioPost
        fields = ['title', 'audio_file']

@login_required
def upload_audio(request):
    if request.method == 'POST':
        form = AudioPostForm(request.POST, request.FILES)
        if form.is_valid():
            audio_post = form.save(commit=False)
            audio_post.user = request.user
            audio_post.save()
            return redirect('home')
    else:
        form = AudioPostForm()
    return render(request, 'upload_audio.html', {'form': form})




