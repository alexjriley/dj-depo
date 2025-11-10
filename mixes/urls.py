from django.urls import path
from .views import home_page_view, upload_audio, signup
from . import views

urlpatterns = [
    path("", home_page_view, name="home"),
    path("upload/", upload_audio, name="upload_audio"),
    path("signup/", signup, name="signup"),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),
    path('post/<int:pk>/edit/', views.edit_audio_post, name='edit_audio_post'),
]
