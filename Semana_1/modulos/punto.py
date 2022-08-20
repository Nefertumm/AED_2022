# Ejercicio 2

from numbers import Number
import Utils.exceptions as cex

class Punto:
    def __init__(self, x: Number = 0, y: Number = 0) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> Number:
        """Getter x"""
        return self._x

    @x.setter
    def x(self, new_x: Number) -> None:
        """Setter x"""
        if not isinstance(new_x, Number):
            raise cex.ValueNotNumber(new_x, 'x no es un número.')
        
        self._x = new_x

    @property
    def y(self) -> Number:
        """Getter y"""
        return self._y

    @y.setter
    def y(self, new_y: Number) -> None:
        """Setter y"""
        if not isinstance(new_y, Number):
            raise cex.ValueNotNumber(new_y, 'y no es un número.')
        
        self._y = new_y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'