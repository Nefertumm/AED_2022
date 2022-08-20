# Ejercicio 6

import unittest
from Semana_1.modulos.producto import Producto

class TestProducto(unittest.TestCase):
    def setUp(self):
        self.p1 = Producto('Cartas', 10, 30)

    def test_descuentos(self):
        self.assertAlmostEqual(self.p1.aplicar_descuento(10), 9, 2) # almost equal porque es float
    
    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()