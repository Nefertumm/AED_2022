from multiprocessing.sharedctypes import Value


class CalculadoraIMC:
    def __init__(self, peso: float, altura: float) -> None:
        self.peso = peso
        self.altura = altura

        self.imc = self.peso / (self.altura ** 2)

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
        try:
            new_peso = float(new_peso)
        except ValueError:
            print('El peso debe ser un número')
            exit(-1)
        
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
        try:
            new_altura = float(new_altura)
        except ValueError:
            print('La altura debe ser un número')
            exit(-1)
        
        if new_altura <= 0:
            raise Exception('La altura debe ser un número no nulo positivo')

        self._altura = new_altura

    def __str__(self):
        result = f'Tu IMC {self.imc:.2f} '
        if self.imc <= 18.5:
            result += "está 'Debajo de lo normal'"
        elif self.imc > 18.5 and self.imc <= 25:
            result += "es 'Normal'"
        elif self.imc > 25 and self.imc <= 30:
            result += "indica 'Sobrepeso'"
        else:
            result += "indica 'Obesidad'"
        
        return result