from django.test import TestCase
from django.core.exceptions import ValidationError
from contact.models import ContactMessage

class ContactMessageModelTest(TestCase):
    
    def setUp(self):
        # Setup run before every test method.
        self.valid_message = ContactMessage.objects.create(
            name='John Doe',
            email='test@example.com',
            message='Test message'
        )

    def test_valid_message(self):
        # Test valid message
        self.assertEqual(self.valid_message.name, 'John Doe')
        self.assertEqual(self.valid_message.email, 'test@example.com')
        self.assertEqual(self.valid_message.message, 'Test message')
        self.assertTrue(self.valid_message.created_at)

    def test_invalid_email_format(self):
        # Test invalid email format
        with self.assertRaises(ValidationError):
            ContactMessage.objects.create(
                name='Jane Doe',
                email='invalid-email',  # Invalid email format
                message='Another test message'
            )

