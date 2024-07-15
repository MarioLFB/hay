from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


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


class LoginViewTest(TestCase):
    """
    Test case for the 'login_view' function to verify successful user login,
    including authentication, redirection to 'home', and success message display.
    """
    def setUp(self):
        self.url = reverse('login')  # Reverse URL for the 'login' view

        # Create a test user for logging in
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        # Test login with valid credentials
        data = {
            'username': self.username,
            'password': self.password,
        }

        # Send a POST request to the 'login' view with valid login data
        response = self.client.post(self.url, data)

        # Assert that the HTTP status code of the response is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that after successful login, the view redirects to the 'home' page
        self.assertRedirects(response, reverse('home'))

        # Assert that the user is authenticated after login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        # Assert that a success message is sent as a flash message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # Assert that there is exactly one message
        self.assertEqual(str(messages[0]), 'You have successfully logged in.')


class LogoutViewTest(TestCase):
    """
    Test case for the 'logout_view' function to verify successful user logout,
    including redirection to 'home' and success message display.
    """
    def setUp(self):
        self.url = reverse('logout')  # Reverse URL for the 'logout' view

        # Create a test user and log them in
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_logout_success(self):
        # Test logout
        response = self.client.post(self.url)

        # Assert that the HTTP status code of the response is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that after successful logout, the view redirects to the 'home' page
        self.assertRedirects(response, reverse('home'))

        # Assert that the user is not authenticated after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)

        # Assert that a success message is sent as a flash message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # Assert that there is exactly one message
        self.assertEqual(str(messages[0]), 'You have successfully logged out.')


class ProfileViewTest(TestCase):
    """
    Test case for the 'profile' view to verify successful profile update,
    including updating user data, redirection to 'profile', and success message display.
    """
    def setUp(self):
        self.url = reverse('profile')  # URL for the 'profile' view

        # Create a test user and log them in
        self.username = 'testuser'
        self.email = 'test@sample.com'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_profile_update_success(self):
        # Test profile update with valid data
        data = {
            'username': 'newusername',
            'email': 'test@test.com',
            'password': 'newpassword123',
            'password_confirm': 'newpassword123',
        }
        
        response = self.client.post(self.url, data)

        # Update the user object from the database
        self.user.refresh_from_db()

        # Verify that the user data has been updated
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'test@test.com')