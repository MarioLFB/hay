from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login


class RegisterViewTest(TestCase):
    """
    Test case for the 'register' view to verify successful user registration,
    including database creation, redirection to login, and success message display.
    """
    def setUp(self):
        self.url = reverse('register') # Reverse URL for the 'register' view

    def test_register_success(self):
        # Reverse URL for the 'register' view
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'password_confirm': 'password123'
        }
        # Send a POST request to the 'register' view with valid registration data
        response = self.client.post(self.url, data)

        # Assert that the HTTP status code of the response is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that after successful registration, the view redirects to the 'login' page
        self.assertRedirects(response, reverse('login'))

        # Assert that a user with username 'newuser' exists in the database
        self.assertTrue(User.objects.filter(username='newuser').exists())

        # Assert that a success message is sent as a flash message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # Assert that there is exactly one message
        self.assertEqual(str(messages[0]), 'You have successfully registered. Please login.')

