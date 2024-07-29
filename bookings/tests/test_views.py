from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Table


class BookingTableViewTest(TestCase):
    """Tests for the views in the bookings app,
    including booking creation, editing, deletion,
    and authentication checks for various user scenarios."""

    def setUp(self):
        """
        Set up the client and create a test user.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_booking_table_authenticated_user(self):
        """
        Test booking table for an authenticated user.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('bookings'))
        self.assertEqual(response.status_code, 200)

    def test_booking_table_unauthenticated_user(self):
        """Test booking table for an unauthenticated user."""
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)

    def test_booked_view(self):
        """Test booked view."""
        response = self.client.get(reverse('booked'))
        self.assertEqual(response.status_code, 200)

    def test_my_bookings_view(self):
        """Test my bookings view."""
        response = self.client.get(reverse('mybookings'))
        self.assertEqual(response.status_code, 302)

    def test_edit_bookings_view(self):
        """Test edit bookings view."""
        booking = Table.objects.create(user=self.user, table_capacity=4)
        response = self.client.get(reverse('edit-bookings', args=[booking.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_bookings_view(self):
        """Test delete bookings view."""
        response = self.client.get(reverse('delete-bookings'))
        self.assertEqual(response.status_code, 200)

    def test_login_needed_view(self):
        """Test login needed view."""
        response = self.client.get(reverse('login_needed'))
        self.assertEqual(response.status_code, 200)
