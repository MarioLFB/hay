from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class RegisterViewTest(TestCase):
    """
    Test case for the 'register' view to verify
    successful user registration, including database creation,
    redirection to login, and success message display.
    """
    def setUp(self):
        self.url = reverse('register')

    def test_register_success(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'password_confirm': 'password123'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('login'))

        self.assertTrue(User.objects.filter(username='newuser').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'You have successfully registered. Please login.'
        )


class LoginViewTest(TestCase):
    """
    Test case for the 'login_view' function to
    verify successful user login, including authentication,
    redirection to 'home', and success message display.
    """
    def setUp(self):
        self.url = reverse('login')

        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_success(self):
        data = {
            'username': self.username,
            'password': self.password,
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('home'))

        self.assertTrue(response.wsgi_request.user.is_authenticated)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully logged in.')


class LogoutViewTest(TestCase):
    """
    Test case for the 'logout_view' function to verify successful user logout,
    including redirection to 'home' and success message display.
    """
    def setUp(self):
        self.url = reverse('logout')

        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.client.login(username=self.username, password=self.password)

    def test_logout_success(self):
        # Test logout
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('home'))

        self.assertFalse(response.wsgi_request.user.is_authenticated)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have successfully logged out.')


class ProfileViewTest(TestCase):
    """
    Test case for the 'profile' view to verify successful
    profile update, including updating user data, redirection
    to 'profile', and success message display.
    """
    def setUp(self):
        self.url = reverse('profile')

        self.username = 'testuser'
        self.email = 'test@sample.com'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.client.login(username=self.username, password=self.password)

    def test_profile_update_success(self):
        data = {
            'username': 'newusername',
            'email': 'test@test.com',
            'password': 'newpassword123',
            'password_confirm': 'newpassword123',
        }

        response = self.client.post(self.url, data)

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'test@test.com')
