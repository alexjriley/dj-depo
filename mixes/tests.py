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

class EditAudioPostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')
        self.audio_post = AudioPost.objects.create(
            user=self.user,
            title='Test Audio',
            description='Test Description',
            audio_file=SimpleUploadedFile('test.mp3', b'12345')  # Include audio_file for validation
        )

    def test_edit_audio_post_view(self):
        response = self.client.get(reverse('edit_audio_post', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_audio_post(self):
        response = self.client.post(reverse('edit_audio_post', args=[self.audio_post.id]), {
            'title': 'Updated Audio',
            'description': 'Updated Description',
            'audio_file': self.audio_post.audio_file  # Ensure audio_file is included
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.audio_post.refresh_from_db()
        self.assertEqual(self.audio_post.title, 'Updated Audio')
        self.assertEqual(self.audio_post.description, 'Updated Description')

class DeleteAudioPostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')
        self.audio_post = AudioPost.objects.create(user=self.user, title='Test Audio')

    def test_delete_audio_post_view(self):
        response = self.client.get(reverse('post-delete', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_audio_post(self):
        response = self.client.post(reverse('post-delete', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertFalse(AudioPost.objects.filter(id=self.audio_post.id).exists())