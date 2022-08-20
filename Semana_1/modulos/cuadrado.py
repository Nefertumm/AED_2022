# Ejercicio 1

import Utils.exceptions as cex

class Cuadrado:
    def __init__(self, lado : float) -> None:
        self.lado = lado

    @property
    def lado(self) -> float:
        """Getter lado"""
        return self._lado

    @lado.setter
    def lado(self, new_lado: float) -> None:
        """Setter lado

        Args:
            new_lado (float): Nueva medida para el lado del cuadrado, en metros
                              Número real > 0
        """
        if not isinstance(new_lado, cex.NumericNotComplex):
            raise cex.ValueNotNumber(new_lado, 'El lado debe ser un número.')
        if new_lado <= 0:
            raise cex.ValueEqualsOrBelowZero(new_lado, 'El lado no puede ser menor o igual a cero.')
        
        self._lado = float(new_lado)

    @property
    def area(self) -> float:
        """Calculo del área del cuadrado

        Returns:
            float: Área del cuadrado
        """
        return round(self.lado ** 2, 2)

    @property
    def perimetro(self) -> float:
        """Cálculo del perímetro del cuadrado

        Returns:
            float: Perímetro del cuadrado
        """
        return round(self.lado * 4, 2)

    def __str__(self):
        return f'Área: {self.area} \nPerímetro: {self.perimetro}'