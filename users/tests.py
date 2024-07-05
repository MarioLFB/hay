from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class SimpleTestCase(TestCase):

    def test_one_equals_one(self):
        # Teste simples para verificar se 1 é igual a 1
        self.assertEqual(1, 1)


