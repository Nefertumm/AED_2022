# Ejercicio 9

import unittest
from Semana_1.modulos.conversor import ConversorTemperatura
import Utils.exceptions as cex

class TestConversor(unittest.TestCase):
    def setUp(self) -> None:
        self.conversor = ConversorTemperatura()

    def test_excepciones(self):
        with self.assertRaises(cex.ValueBelowZero):
            self.conversor.convertir_a(-10, 'K', 'C')
        with self.assertRaises(ValueError):
            self.conversor.convertir_a(100, 'C', 'B')

    def test_conversor(self):
        self.assertAlmostEqual(self.conversor.convertir_a(0, 'C', 'K'), 273.15, 2)
        self.assertAlmostEqual(self.conversor.convertir_a(212, 'F', 'C'), 100, 2)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()