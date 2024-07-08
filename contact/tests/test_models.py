from django.test import TestCase
from django.core.exceptions import ValidationError
from contact.models import ContactMessage

class ContactMessageModelTest(TestCase):
    """
    Test case for ContactMessage model to validate its attributes and behavior.
    """
    def setUp(self):
        # Setup run before every test method.
        # Create a valid ContactMessage instance for testing
        self.valid_message = ContactMessage.objects.create(
            name='John Doe',
            email='test@example.com',
            message='Test message'
        )

    def test_valid_message(self):
        # Test case to verify attributes of a valid ContactMessage instance
        self.assertEqual(self.valid_message.name, 'John Doe')
        self.assertEqual(self.valid_message.email, 'test@example.com')
        self.assertEqual(self.valid_message.message, 'Test message')
        self.assertTrue(self.valid_message.created_at)

    def test_invalid_email_format(self):
        # Test case to verify handling of invalid email format
        with self.assertRaises(ValidationError):
            # Attempt to create a ContactMessage with an invalid email format
            ContactMessage.objects.create(
                name='Jane Doe',
                email='invalid-email',  # Invalid email format
                message='Another test message'
            )

