# Ejercicio 6

import Utils.exceptions as cex

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def nombre(self) -> str:
        """nombre getter"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        """nombre setter
        -------------
            new_nombre: str
                str no vacia
        """
        if type(new_nombre) != str:
            raise cex.ValueNotString(new_nombre)
        if not new_nombre.strip():
            raise cex.ValueEmptyString('Nombre no puede ser nulo')
        self._nombre = new_nombre
    
    @property
    def precio(self) -> float:
        """precio getter"""
        return self._precio

    @precio.setter
    def precio(self, new_precio: float) -> None:
        """precio setter
        -------------
            new_precio: float or int
                flotante o entero positivo no nulo
        """
        if new_precio <= 0:
            raise cex.ValueBelowZero(new_precio)

        self._precio = new_precio
    
    @property
    def cantidad(self) -> float:
        """getter cantidad"""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, new_cantidad: int) -> None:
        """cantidad setter
        -------------
            new_cantidad: int
                entero positivo no nulo
        """
        if new_cantidad < 0:
            raise cex.ValueBelowZero(new_cantidad)
        self._cantidad = new_cantidad

    def aplicar_descuento(self, descuento : float) -> float:
        """aplica un descuento sobre el precio del producto dado el valor porcentual"""
        if (descuento <= 0):
            raise cex.ValueBelowZero(descuento)
        
        self.precio -= self.precio * descuento / 100
        return self.precio

    def __str__(self):
        return f'Producto: {self.nombre} - ${self.precio} - Cantidad: {self.cantidad}'
