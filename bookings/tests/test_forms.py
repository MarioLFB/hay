from django.test import TestCase
from bookings.forms import TableForm
from datetime import date


class TableFormTest(TestCase):
    """
    Test cases for TableForm to validate form validation and saving functionality.
    """
    def test_valid_form(self):
        # Validates a valid TableForm instance.
        form_data = {
            'table_name': 'Table 1',
            'table_phone': '1234567890',
            'table_email': 'test@test.com',
            'table_capacity': 4,
            'table_date': '2021-01-01',
            'table_time': '12:00'
        }
        form = TableForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Validates an invalid TableForm instance with invalid email format.
        form_data = {
            'table_name': 'Table 1',
            'table_phone': '1234567890',
            'table_email': 'invalid-email',
            'table_capacity': 4,
            'table_date': '2021-01-01',
            'table_time': '12:00'
        }
        form = TableForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_save_method(self):
        # Validates saving functionality of TableForm.
        form_data = {
            'table_name': 'Table 1',
            'table_phone': '1234567890',
            'table_email': 'test@test.com',
            'table_capacity': 4,
            'table_date': date.today(),
            'table_time': '12:00'
        }
        form = TableForm(data=form_data)
        self.assertTrue(form.is_valid())

        table = form.save()
        self.assertEqual(table.table_name, 'Table 1')
        self.assertEqual(table.table_phone, '1234567890')
        self.assertEqual(table.table_email, 'test@test.com')
        self.assertEqual(table.table_capacity, 4)
        self.assertEqual(table.table_date, date.today())
        self.assertEqual(table.table_time.strftime('%H:%M'), '12:00')
