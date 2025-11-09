# pylint: disable=no-member

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import AudioPost

class AudioPostModelTest(TestCase):
    """
    Test suite for the `AudioPost` model.
    """

    def test_create_audio_post(self):
        """
        Test the creation of an `AudioPost` instance.

        This test ensures that an `AudioPost` object can be created with valid data and that its fields are correctly set.
        """
        user = User.objects.create_user(username='testuser', password='testpass')
        post = AudioPost.objects.create(user=user, title='Test Audio', audio_file=SimpleUploadedFile('test.mp3', b'12345'))
        self.assertEqual(post.title, 'Test Audio')
        self.assertEqual(post.user.username, 'testuser')

    def test_audio_post_str(self):
        """
        Test the string representation of the `AudioPost` model.

        This test ensures that the `__str__` method of the `AudioPost` model returns
        the expected string.
        """
        user = User.objects.create_user(username='testuser', password='testpass')
        post = AudioPost.objects.create(user=user, title='Test Audio')
        self.assertEqual(str(post), "Test Audio by testuser")

class HomePageViewTest(TestCase):
    """
    Test suite for the home page view.

    This class contains tests to verify the functionality of the home page view,
    including its status code and accessibility.
    
    Methods:
        - test_homepage_status_code: Ensures the home page returns a 200 status code.
    """

    def test_homepage_status_code(self):
        """
        Test the status code of the home page.

        This test ensures that the home page view returns a 200 HTTP status code,
        indicating that the page is accessible.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class UploadAudioViewTest(TestCase):
    """
    Test suite for the upload audio view.

    This class contains tests to verify the functionality of the upload audio view,
    including login requirements and successful audio uploads.
    
    Methods:
        - setUp: Sets up a test user and client for the tests.
        - test_upload_requires_login: Ensures the upload view redirects unauthenticated users.
        - test_upload_audio: Verifies that an authenticated user can upload audio successfully.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user and initializes the test client for use
        in the upload audio view tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()

    def test_upload_requires_login(self):
        """
        Test that the upload view requires login.

        This test ensures that unauthenticated users are redirected to the login page
        when attempting to access the upload audio view.
        """
        response = self.client.get(reverse('upload_audio'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_upload_audio(self):
        """
        Test the audio upload functionality.

        This test verifies that an authenticated user can successfully upload an audio file
        and that the audio post is created in the database.
        """
        self.client.login(username='testuser', password='testpass')
        audio = SimpleUploadedFile('test.mp3', b'12345')
        response = self.client.post(reverse('upload_audio'), {'title': 'Test', 'audio_file': audio})
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertTrue(AudioPost.objects.filter(title='Test').exists())

class EditAudioPostViewTest(TestCase):
    """
    Test suite for the edit audio post view.

    This class contains tests to verify the functionality of editing an audio post,
    including accessing the edit view and updating the post details.
    
    Methods:
        - setUp: Sets up a test user, client, and an audio post for the tests.
        - test_edit_audio_post_view: Ensures the edit view is accessible.
        - test_edit_audio_post: Verifies that an audio post can be updated successfully.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user, initializes the test client, and creates
        an audio post for use in the edit audio post view tests.
        """
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
        """
        Test the accessibility of the edit audio post view.

        This test ensures that the edit audio post view is accessible and returns
        a 200 HTTP status code.
        """
        response = self.client.get(reverse('edit_audio_post', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_audio_post(self):
        """
        Test the functionality of editing an audio post.

        This test verifies that an audio post can be successfully updated with new
        title and description values.
        """
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
    """
    Test suite for the delete audio post view.

    This class contains tests to verify the functionality of deleting an audio post,
    including accessing the delete view and successfully deleting the post.
    
    Methods:
        - setUp: Sets up a test user, client, and an audio post for the tests.
        - test_delete_audio_post_view: Ensures the delete view is accessible.
        - test_delete_audio_post: Verifies that an audio post can be deleted successfully.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user, initializes the test client, and creates
        an audio post for use in the delete audio post view tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')
        self.audio_post = AudioPost.objects.create(user=self.user, title='Test Audio')

    def test_delete_audio_post_view(self):
        """
        Test the accessibility of the delete audio post view.

        This test ensures that the delete audio post view is accessible and returns
        a 200 HTTP status code.
        """
        response = self.client.get(reverse('post-delete', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_audio_post(self):
        """
        Test the functionality of deleting an audio post.

        This test verifies that an audio post can be successfully deleted and
        removed from the database.
        """
        response = self.client.post(reverse('post-delete', args=[self.audio_post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertFalse(AudioPost.objects.filter(id=self.audio_post.id).exists())

class IntegrationTests(TestCase):
    """
    Integration tests for workflows involving multiple components.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user and initializes the test client for use
        in the integration tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_full_audio_post_workflow(self):
        """
        Test creating, editing, and deleting an audio post.

        This test verifies the entire workflow of creating an audio post, editing its
        details, and deleting it, ensuring that all steps function correctly together.
        """
        # Create an audio post
        audio = SimpleUploadedFile('test.mp3', b'12345')
        response = self.client.post(reverse('upload_audio'), {'title': 'Test', 'audio_file': audio})
        self.assertEqual(response.status_code, 302)
        post = AudioPost.objects.get(title='Test')

        # Edit the audio post
        response = self.client.post(reverse('edit_audio_post', args=[post.id]), {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'audio_file': post.audio_file
        })
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Title')

        # Delete the audio post
        response = self.client.post(reverse('post-delete', args=[post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(AudioPost.objects.filter(id=post.id).exists())

class ErrorHandlingTests(TestCase):
    """
    Tests for error handling in the application.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user and initializes the test client for use
        in the error handling tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_404_error(self):
        """
        Test that a 404 error is returned for a nonexistent URL.

        This test ensures that requesting a URL that does not exist in the application
        returns a 404 HTTP status code.
        """
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_form_submission(self):
        """
        Test that invalid form submissions are handled gracefully.

        This test verifies that submitting a form with invalid data (e.g., empty required fields)
        does not crash the application and returns the user to the form with error messages.
        """
        response = self.client.post(reverse('upload_audio'), {'title': '', 'audio_file': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'audio_file', 'This field is required.')