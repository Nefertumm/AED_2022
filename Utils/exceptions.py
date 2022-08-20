from typing import TypeAlias
from numpy import number

NumericNotComplex: TypeAlias = int | float | number #Union[int, float, number]

class ValueBelowZero(Exception):
    """Usado para valores que no deben ser menores que cero"""
    def __init__(self, value : NumericNotComplex, message : str = 'El valor no puede ser menor que cero.') -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'

class ValueEqualsOrBelowZero(Exception):
    """Usado para valores que no deben ser iguales o menores que cero"""
    def __init__(self, value : NumericNotComplex, message : str = 'El valor no puede ser igual o menor que cero.') -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'

class ValueNotString(Exception):
    """Usado para valores que deben ser obligatoriamente strings"""
    def __init__(self, value, message : str = 'El valor debe ser un string.') -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'

class ValueEmptyString(Exception):
    """Usado para valores que son strings vacías"""
    def __init__(self, message : str = 'El valor no puede ser un string vacío.') -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class ValueNotNumber(Exception):
    """Usado para valores que no son números"""
    def __init__(self, value, message : str = 'El valor debe ser un número.') -> None:
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'