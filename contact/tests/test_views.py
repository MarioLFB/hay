from django.urls import reverse
from django.test import TestCase

class ContactViewTests(TestCase):
    """
    Test cases for Contact views to ensure correct template rendering and HTTP response codes.
    """

    def test_contact_view(self):
        # Verifies rendering and HTTP response for the 'contact' view.
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_message_sent_view(self):
        # Verifies rendering and HTTP response for the 'message_sent' view.
        response = self.client.get(reverse('message_sent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/message_sent.html')