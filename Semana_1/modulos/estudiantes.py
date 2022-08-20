# Ejercicio 4

import Utils.exceptions as cex

class Estudiante:
    def __init__(self, legajo: int, apellido: str, nombre: str, documento: int, promedio: float) -> None:
        self.legajo = legajo
        self.apellido = apellido
        self.nombre = nombre
        self.documento = documento
        self.promedio = promedio
    
    @property
    def legajo(self) -> int:
        """legajo getter"""
        return self._legajo
    
    @legajo.setter
    def legajo(self, new_legajo: int) -> None:
        """legajo setter
        -------------
            new_legajo: int
                entero positivo
        """
        if not isinstance(new_legajo, cex.NumericNotComplex):
            raise cex.ValueNotNumber(new_legajo, 'El legajo debe ser un número')
        if new_legajo <= 0:
            raise cex.ValueEqualsOrBelowZero(new_legajo, 'El legajo debe ser un número positivo')
        
        self._legajo = int(new_legajo)
        
    @property
    def apellido(self) -> str:
        """apellido getter"""
        return self._apellido
    
    @apellido.setter
    def apellido(self, new_apellido: str) -> None:
        """apellido setter
        -------------
            new_apellido: str
                string no vacio
        """
        if type(new_apellido) != str:
            raise cex.ValueNotString(new_apellido, 'El apellido debe ser un string')
        if not new_apellido.strip():
            raise cex.ValueEmptyString(new_apellido.strip(), 'No se permite que el apellido sea nulo')
        
        self._apellido = new_apellido
        
    @property
    def nombre(self) -> str:
        """nombre getter"""
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre : str) -> None:
        """nombre setter
        -------------
            new_nombre: str
                string no vacio
        """
        if type(new_nombre) != str:
            raise cex.ValueNotString(new_nombre, 'El nombre debe ser un string')
        if not new_nombre.strip():
            raise cex.ValueEmptyString(new_nombre.strip(), 'No se permite que el nombre sea nulo')
        self._nombre = new_nombre
        
    @property
    def documento(self) -> int:
        """documento getter"""
        return self._documento
    
    @documento.setter
    def documento(self, new_documento : int) -> None:
        """documento setter
        -------------
            new_documento: int
                entero positivo
        """
        if type(new_documento) != int:
            raise cex.ValueNotNumber(new_documento, 'El documento debe ser un número')
        if new_documento <= 0:
            raise cex.ValueEqualsOrBelowZero(new_documento, 'No se permite que el documento sea nulo o negativo')
        self._documento = new_documento
        
    @property
    def promedio(self) -> float:
        """promedio getter"""
        return self._promedio
    
    @promedio.setter
    def promedio(self, new_promedio : float) -> None:
        """promedio setter
        -------------
            new_promedio: float/int
                float o entero positivo
        """
        if not isinstance(new_promedio, cex.NumericNotComplex):
            raise cex.ValueNotNumber(new_promedio, 'El promedio debe ser un número')
        if new_promedio <= 0:
            raise cex.ValueEqualsOrBelowZero(new_promedio, 'No se permite que el promedio sea nulo o negativo')
        self._promedio = float(new_promedio) # cast en caso de cualquier otra cosa que no sea entero
