from django.urls import path
from .views import home_page_view, upload_audio, signup

urlpatterns = [
    path("", home_page_view, name="home"),
    path("upload/", upload_audio, name="upload_audio"),
    path("signup/", signup, name="signup"),
]