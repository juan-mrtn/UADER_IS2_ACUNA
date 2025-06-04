"""
Resultado Miercoles 21 de Mayo
juanacuna@MacBook-de-Juan TP6 % pylint new_primes_v4.py 
************* Module new_primes_v4
new_primes_v4.py:1:0: C0114: Missing module docstring (missing-module-docstring)
new_primes_v4.py:8:0: C0115: Missing class docstring (missing-class-docstring)
new_primes_v4.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
new_primes_v4.py:8:0: R0903: Too few public methods (1/2) (too-few-public-methods)
new_primes_v4.py:41:0: C0115: Missing class docstring (missing-class-docstring)
new_primes_v4.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
new_primes_v4.py:55:4: C0116: Missing function or method docstring (missing-function-docstring)
new_primes_v4.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 8.49/10"""

import unittest
from types import SimpleNamespace

from new_primes_v4 import Rango, CalculadoraPrimos  # Asegurate de que el archivo principal se llame `primos.py`

class TestRango(unittest.TestCase):

    def test_rango_por_defecto(self):
        rango = Rango(["script.py"])
        self.assertEqual(rango.lower, 1)
        self.assertEqual(rango.upper, 50)
        self.assertTrue(rango.es_valido())

    def test_rango_un_argumento(self):
        rango = Rango(["script.py", "30"])
        self.assertEqual(rango.lower, 1)
        self.assertEqual(rango.upper, 30)
        self.assertTrue(rango.es_valido())

    def test_rango_dos_argumentos(self):
        rango = Rango(["script.py", "10", "20"])
        self.assertEqual(rango.lower, 10)
        self.assertEqual(rango.upper, 20)
        self.assertTrue(rango.es_valido())

    def test_rango_negativo(self):
        rango = Rango(["script.py", "-5", "20"])
        self.assertFalse(rango.es_valido())

    def test_rango_fuera_de_limite(self):
        rango = Rango(["script.py", "1", "70000"])
        self.assertFalse(rango.es_valido())

    def test_rango_invertido(self):
        rango = Rango(["script.py", "30", "10"])
        self.assertFalse(rango.es_valido())


class TestCalculadoraPrimos(unittest.TestCase):

    def setUp(self):
        # Creamos un rango "mock" usando SimpleNamespace
        self.rango = SimpleNamespace(lower=1, upper=10)
        self.calc = CalculadoraPrimos(self.rango)

    def test_es_primo(self):
        self.assertFalse(self.calc.es_primo(0))
        self.assertFalse(self.calc.es_primo(1))
        self.assertTrue(self.calc.es_primo(2))
        self.assertTrue(self.calc.es_primo(3))
        self.assertFalse(self.calc.es_primo(4))
        self.assertTrue(self.calc.es_primo(5))
        self.assertFalse(self.calc.es_primo(9))
        self.assertTrue(self.calc.es_primo(7))

if __name__ == '__main__':
    unittest.main()
