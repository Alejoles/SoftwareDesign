import unittest

from calculadora import suma
from calculadora import resta
from calculadora import get_users


class CalculadoraTest(unittest.TestCase):

    def setUp(self) -> None:
        self.numero1 = 2
        self.numero2 = 2

    def test_suma_ok(self):

        resultado = suma(self.numero1, self.numero2)
        print(resultado)
        self.assertEqual(resultado, self.numero1 + self.numero2)

    def test_resta(self):
        resultado = resta(self.numero1, self.numero2)
        self.assertEqual(resultado, 0)

    def test_get_users(self):
        response = get_users()
        mock = {"nombre": "alejo", "edad": 1}
        mock_key = list(mock)
        response_key = list(response)
        self.assertEqual(mock_key, response_key)
