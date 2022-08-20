import unittest
from modulos.calculadoraimc import CalculadoraIMC

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.imc1 = CalculadoraIMC(80, 1.8)
    
    def test_calculadora(self):
        self.assertEqual(self.imc1.calcular_imc(), "Tu IMC 24.69 es 'Normal'")
        
if __name__ == '__main__':
    unittest.main()