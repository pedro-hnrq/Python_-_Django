from django.test import TestCase
from ..models import Usuario

class UsuarioTestCase(TestCase):

    def setUp(self):
        Usuario.objects.create(nome='henrique', email="henrique@gmail.com", senha="1234")
        
    def test_models_criado_no_banco(self):
        usuario = Usuario.objects.get(nome='henrique')

        #Igualdade
        self.assertEqual(usuario.__str__(), 'henrique')

    def test_add_pontos(self):
        usuario = Usuario.objects.get(nome='henrique')
        usuario.add_pontos()


        self.assertEqual(usuario.pontos, 10)


        # self.assertEqual(x, y) # x == y
        # self.assertNotEqual (x, y) # x != y
        # self.assertTrue(x, y) #bool(x) is True
        # self.assertFalse(x, y) #bool(x) is False
        # self.assertIs(x, y) # x is y
        # self.assertIsNot(x, y) # x is not y
        # self.assertIsNone(x, y) # x is None
        # self.assertIn(x, y) # x in y
        # self.assertNotIn(x, y) # x not in y
        # self.assertIsInstance(5, Usuario) # isinstance(x, y)
        # self.assertNotIsInstance(5, Usuario) # not isinstance (x, y)

        # self.assertGreater(x, y) # x > b
        # self.assertGreaterEqual(x, y) # x >= y
        # self.assertLess(x, y) # x < y 
        # self.assertLessEqual(x, y) # x <= y

        