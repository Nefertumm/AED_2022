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
        if type(new_text) != str:
            raise Exception('El texto debe ser un string')
        
        self._text = new_text

    def depurar_texto(self) -> None:
        """Elimina los caracteres ',', '.', ':', ';', '-', '_' del texto"""
        dep = [',', '.', ':', ';', '-', '_']
        temp = self.text
        for char in dep:
            temp = temp.replace(char, '')
        
        temp.split(' ')
        temp = [c for c in temp if c.strip()]
        print(temp)
        self.text = ' '.join(temp)

    def cantidad_palabras(self) -> int:
        """Devuelve la cantidad de palabras en el texto"""
        return len(self.text.split(' '))

    def ocurrencia_palabra(self, palabra: str) -> int:
        """Devuelve la ocurrencia de la palabra en el texto"""
        if type(palabra) != str:
            print('La palabra a buscar debe ser un string')
            try:
                palabra = str(palabra)
            except ValueError:
                print('La palabra a buscar debe poder ser convertible a string')
                exit(-1)
        if not palabra.strip():
            print('La palabra a buscar no debe ser un string vacio')
            return 0
        return self.text.count('palabra')

    def __str__(self):
        return self.text