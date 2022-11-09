
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_status_code_200(self):
        response = self.client.get(f'{self.url}?id=1')
        self.assertEqual(response.status_code, 200)
