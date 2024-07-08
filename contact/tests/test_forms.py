from django.test import TestCase
from contact.forms import ContactForm

class ContactFormTest(TestCase):
    """
    Test cases for ContactForm to validate form validation and saving functionality.
    """
    def test_valid_form(self):
        # Validates a valid ContactForm instance.
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Validates an invalid ContactForm instance with invalid email format.
        form_data = {
            'name': 'John Doe',
            'email': 'invalid-email',  # Invalid email format
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_save_method(self):
        # Validates saving functionality of ContactForm.
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

        contact_message = form.save()
        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'johndoe@example.com')
        self.assertEqual(contact_message.message, 'Hello, this is a test message.')
