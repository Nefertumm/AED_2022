class CalculadoraIMC:
    def __init__(self, peso: float, altura: float) -> None:
        self.peso = peso
        self.altura = altura

    @property
    def peso(self) -> float:
        """getter peso"""
        return self._peso

    @peso.setter
    def peso(self, new_peso: float) -> None:
        """setter de peso
        ----------
        new_peso : float
            numero flotante positivo no nulo, expresado en kilogramos
        """        
        if new_peso <= 0:
            raise Exception('El peso no debe ser negativo o nulo')
        
        self._peso = new_peso

    @property
    def altura(self) -> float:
        """getter altura"""
        return self._altura
    
    @altura.setter
    def altura(self, new_altura: float) -> None:
        """setter de altura
        ----------
        new_altura : float
            numero flotante positivo no nulo, expresado en metros
        """
        
        if new_altura <= 0:
            raise Exception('La altura debe ser un número no nulo positivo')

        self._altura = new_altura
        
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        result = f'Tu IMC {imc:.2f} '
        if imc <= 18.5:
            result += "está 'Debajo de lo normal'"
        elif imc > 18.5 and imc <= 25:
            result += "es 'Normal'"
        elif imc > 25 and imc <= 30:
            result += "indica 'Sobrepeso'"
        else:
            result += "indica 'Obesidad'"
        
        return result

    def __str__(self):
        return self.calcular_imc()