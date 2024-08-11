from django.test import TestCase
from django.core.exceptions import ValidationError
from contact.models import ContactMessage


class ContactMessageModelTest(TestCase):
    """
    Test case for ContactMessage model to
    validate its attributes and behavior.
    """

    def setUp(self):
        self.valid_message = ContactMessage.objects.create(
            name='John Doe',
            email='test@example.com',
            message='Test message'
        )

    def test_valid_message(self):
        self.assertEqual(self.valid_message.name, 'John Doe')
        self.assertEqual(self.valid_message.email, 'test@example.com')
        self.assertEqual(self.valid_message.message, 'Test message')
        self.assertTrue(self.valid_message.created_at)

    def test_invalid_email_format(self):
        with self.assertRaises(ValidationError):

            ContactMessage.objects.create(
                name='Jane Doe',
                email='invalid-email',
                message='Another test message'
            )
