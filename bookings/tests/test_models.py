from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, time  # Import time from datetime module
from bookings.models import Table

class TableTest(TestCase):
    """Tests functionalities of the Table model."""
    
    def setUp(self):
         # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.table_data = {
            'table_name': 'Table 1',
            'table_phone': '+44 20 7123 4567',
            'table_email': 'email@email.com',
            'table_capacity': 4,
            'table_date': date.today(),
            'table_time': time(hour=8, minute=0, second=0),
            'user': self.user,
        }
    
    def test_create_table(self):
        # Test creating a table in the database
        table = Table.objects.create(**self.table_data)
        
        self.assertEqual(table.table_name, self.table_data['table_name'])
        self.assertEqual(table.table_phone, self.table_data['table_phone'])
        self.assertEqual(table.table_email, self.table_data['table_email'])
        self.assertEqual(table.table_capacity, self.table_data['table_capacity'])
        self.assertEqual(table.table_date, self.table_data['table_date'])
        self.assertEqual(table.table_time.strftime('%H:%M:%S'), self.table_data['table_time'].strftime('%H:%M:%S'))
        self.assertEqual(table.user, self.table_data['user'])
    
    def test_table_str_representation(self):
        # Test the string representation of the table
        table = Table.objects.create(**self.table_data)

        # Assert that __str__ method returns the table name
        self.assertEqual(str(table), self.table_data['table_name'])
