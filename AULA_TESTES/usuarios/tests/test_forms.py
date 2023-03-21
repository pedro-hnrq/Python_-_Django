from django.test import TestCase
from ..forms import FormUsuario
from django.http import HttpRequest

class FormtestCase(TestCase):

    def setUp(self):
        self.form = FormUsuario()

    def test_campos_form(self):
        self.assertIn('nome', self.form.fields)
        self.assertIn('email', self.form.fields)
        self.assertIn('senha', self.form.fields)
        # self.assertIn('pontos', self.form.fields)

    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            'nome': 'henrique',
            'email': 'henrique@gmail.com',
            'senha': '1234'
        }
        form = FormUsuario(request.POST)
        self.assertTrue(form.is_valid())
    