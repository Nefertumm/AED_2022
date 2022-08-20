# Ejercicio 8

import Utils.exceptions as cex

class AnalizadorTexto:
    def __init__(self, text: str) -> None:
        self.text = text

    @property
    def text(self) -> str:
        """getter text"""
        return self._text

    @text.setter
    def text(self, new_text: str):
        """text setter
        -------------
            new_text: str
        """
        if not isinstance(new_text, str):
            raise cex.ValueNotString(new_text, 'El texto debe ser un string')
        if not new_text.strip():
            raise cex.ValueEmptyString('El texto no puede ser solo caracteres vacíos.')
        
        self._text = new_text

    def depurar_texto(self) -> None:
        """Elimina los caracteres ',', '.', ':', ';', '-', '_' del texto"""
        dep = [',', '.', ':', ';', '-', '_']
        temp = self.text
        for char in dep:
            temp = temp.replace(char, ' ')
        
        temp = temp.split(' ')
        temp = [c for c in temp if c.strip()]
        self.text = ' '.join(temp)

    def cantidad_palabras(self) -> int:
        """Devuelve la cantidad de palabras en el texto"""
        return len(self.text.split(' '))

    def ocurrencia_palabra(self, palabra: str) -> int:
        """Devuelve la ocurrencia de la palabra en el texto"""
        if not isinstance(palabra, str):
            raise cex.ValueNotString(palabra, 'La palabra a buscar debe ser un string')

        return self.text.lower().count(palabra.lower())

    def __str__(self):
        return f'Text: {self.text} \n Cantidad de palabras: {self.cantidad_palabras()}'
