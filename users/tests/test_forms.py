import unittest
from django import forms
from django.test import TestCase
from users.forms import UserRegisterForm


class UserRegisterFormTest(TestCase):

    def test_clean_username_valid(self):
        """
        Tests if the UserRegisterForm validates a user registration correctly with valid data. 
        Verifies that the form accepts a username, email, password, and password confirmation 
        that meet the defined validation criteria.
        """
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Test1234',
            'password_confirm': 'Test1234',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_clean_username_too_short(self):
        """
        Tests if the UserRegisterForm raises a validation error when the username is too short.
        Verifies that the form raises a validation error when the username is less than 5 characters long.
        """
        form = UserRegisterForm(data={'username': 'test'})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'Username must be at least 5 characters long.')

    
    def test_clean_username_too_long(self):
        """
        Tests if the UserRegisterForm raises a validation error when the username is too long.
        Verifies that the form raises a validation error when the username is more than 20 characters long.
        """
        long_username = 'a' * 21
        form = UserRegisterForm(data={'username': long_username})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'Username must be at most 20 characters long.')


    def test_clean_password_confirm_match(self):
        """
        Tests if the UserRegisterForm raises a validation error when the password and password_confirm fields do not match.
        Verifies that the form raises a validation error when the password and password_confirm fields do not match.
        """
        form_data = {
            'password': 'Strong123',
            'password_confirm': 'Strong123',
        }
        form = UserRegisterForm(data=form_data)
        
        # Remove the username and email fields from the form
        form.fields.pop('username', None)
        form.fields.pop('email', None)
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")


    def test_clean_password_confirm_mismatch(self):
        """
        Tests if the UserRegisterForm raises a validation error when the password and password_confirm fields do not match.
        Verifies that the form raises a validation error when the password and password_confirm fields do not match.
        """
        form_data = {
            'password': 'Strong123',
            'password_confirm': 'Different123',
        }
        form = UserRegisterForm(data=form_data)
        
        # remove the username and email fields from the form
        form.fields.pop('username', None)
        form.fields.pop('email', None)
        
        self.assertFalse(form.is_valid())
        self.assertIn('password_confirm', form.errors.keys())
        self.assertEqual(form.errors['password_confirm'][0], 'Passwords do not match.')


if __name__ == '__main__':
    unittest.main()