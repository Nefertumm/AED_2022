# Ejercicio 8

import unittest
from Semana_1.modulos.analizador import AnalizadorTexto

class TestAnalizador(unittest.TestCase):
    def setUp(self) -> None:
        self.analizador = AnalizadorTexto('Esto es-----_-_-_un::::; texto    . . . prueba     ._ .:;.   de__prueba ---------s-s----  ,,prueba,, prue ba  .')
        self.analizador.depurar_texto()

    def test_cantidad_palabras(self):
        self.assertEqual(self.analizador.cantidad_palabras(), 12)

    def test_ocurrencia_palabra(self):
        self.assertEqual(self.analizador.ocurrencia_palabra('prueba'), 3)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()