from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AudioPost
from django.core.files.uploadedfile import SimpleUploadedFile

class AudioPostModelTest(TestCase):
	def test_create_audio_post(self):
		user = User.objects.create_user(username='testuser', password='testpass')
		post = AudioPost.objects.create(user=user, title='Test Audio', audio_file=SimpleUploadedFile('test.mp3', b'12345'))
		self.assertEqual(post.title, 'Test Audio')
		self.assertEqual(post.user.username, 'testuser')

class HomePageViewTest(TestCase):
	def test_homepage_status_code(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

class UploadAudioViewTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.client = Client()

	def test_upload_requires_login(self):
		response = self.client.get(reverse('upload_audio'))
		self.assertEqual(response.status_code, 302)  # Redirect to login

	def test_upload_audio(self):
		self.client.login(username='testuser', password='testpass')
		audio = SimpleUploadedFile('test.mp3', b'12345')
		response = self.client.post(reverse('upload_audio'), {'title': 'Test', 'audio_file': audio})
		self.assertEqual(response.status_code, 302)  # Redirect to home
		self.assertTrue(AudioPost.objects.filter(title='Test').exists())
