# Ejercicio 3

import requests as req
import Utils.exceptions as cex

class Persona:
    def __init__(self, nombre : str, apellido : str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
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
            raise cex.ValueEmptyString(new_nombre.strip(), 'El nombre no puede ser un string vacio')
        self._nombre = new_nombre.capitalize()
    
    @property
    def apellido(self) -> str:
        """apellido getter"""
        return self._apellido
    
    @apellido.setter
    def apellido(self, new_apellido : str) -> None:
        """apellido setter
        -------------
            new_apellido: str
                string no vacio
        """
        if type(new_apellido) != str:
            raise cex.ValueNotString(new_apellido, 'El apellido debe ser un string')
        if not new_apellido.strip():
            raise cex.ValueEmptyString(new_apellido.strip(), 'El apellido no puede ser un string vacio')
        self._apellido = new_apellido.capitalize()
        
# Ejercicio 5

class PersonaAleatoria(Persona):
    def __init__(self):
        api_url = 'http://names.drycodes.com/1?format=json'
        try:
            response = req.get(api_url)
            jsonResStr = response.json()[0].split('_')
            nombre = jsonResStr[0]
            apellido = ' '.join(jsonResStr[1:])
            super().__init__(nombre, apellido)
        except req.exceptions.JSONDecodeError:
            print('La api no devolvió un json x.x')
        except req.exceptions.RequestException:
            print('Algo salió mal x.x')
