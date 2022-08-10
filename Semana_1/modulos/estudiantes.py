# Ejercicio 4

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
        if type(new_legajo) != int:
            raise Exception('El legajo debe ser un entero')
        if new_legajo <= 0:
            raise Exception('No se permiten legajos en nulos o negativos')
        
        self._legajo = new_legajo
        
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
            raise Exception('El apellido debe ser un string')
        if not new_apellido.strip():
            raise Exception('No se permite que el apellido sea nulo')
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
            raise Exception('El nombre debe ser un string')
        if not new_nombre.strip():
            raise Exception('No se permite que el nombre sea nulo')
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
            raise Exception('El documento debe ser un entero')
        if new_documento <= 0:
            raise Exception('No se permite que el documento sea nulo o negativo')
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
        if type(new_promedio) != float or type(new_promedio) != int:
            raise Exception('El promedio debe ser un flotante o un entero')
        if new_promedio <= 0:
            raise Exception('No se permite que el promedio sea nulo o negativo')
        self._promedio = float(new_promedio) # cast en caso de entero
        
        
        