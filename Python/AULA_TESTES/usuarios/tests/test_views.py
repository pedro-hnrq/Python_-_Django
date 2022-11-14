
from pyexpat.errors import messages
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import Usuario
from django.contrib.messages import get_messages

class ViewsTestCase(TestCase):

    def setUp(self):
        Usuario.objects.create(nome='henrique', email="henrique@gmail.com", senha="1234")
        self.client = Client()
        self.url = reverse('home')

    def test_status_code_200(self):
        response = self.client.get(f'{self.url}?email=henrique@gmail.com')
        self.assertEqual(response.status_code, 200)

    def test_status_code_404(self):
        response = self.client.get(f'{self.url}?email=marcos@gmail.com')
        self.assertEqual(response.status_code, 404)

    def test_template_used_home_cond_1(self):
        response = self.client.get(f'{self.url}?email=henrique@gmail.com&cond=1')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_template_used_home_cond_not_1(self):
        response = self.client.get(f'{self.url}?email=henrique@gmail.com&cond=2')
        self.assertTemplateUsed(response, 'logar.html')
    
    def test_message_error_email_gmail(self):
        response = self.client.get(f'{self.url}?email=henrique@hotmail.com&cond=2')
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Informe um email do gmail', messages)