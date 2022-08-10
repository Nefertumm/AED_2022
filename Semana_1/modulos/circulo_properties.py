import math

class Circulo:
    """clase que modela un círculo mediante su atributo radio posee métodos para 
    modificar/obtener el radio y para calcular y devolver su perímetro y su área.
    -----------
    atributos:
        radio: int. valor entero que representa el radio del círculo
    """    
    def __init__(self, radio: int = 0) -> None:       
        self.radio = radio
        
    def get_radio(self) -> int:
        """getter de radio"""
        return self._radio
    
    def set_radio(self, valor : int) -> None:
        """setter de radio
        ----------
        valor : int
            valor entero positivo para modificar el radio.
        """
        if valor >= 0:
            self._radio = valor
        else:
            self._radio = 0
            raise Exception('El valor del radio no puede ser negativo')
        
    def get_area(self) -> float:
        """calcula y retorna el valor del área con 2 decimales de precisión"""
        area = math.pi*self.get_radio()**2
        return round(area, 2)
    
    def get_perimetro(self) -> float:
        """calcula y retorna el valor del perímetro con 2 decimales de precisión"""
        perimetro = 2*math.pi*self.get_radio()
        return round(perimetro, 2)        

    radio = property(fget = get_radio, fset = set_radio, doc = 'propiedad radio')
    
    area = property(fget = get_area, doc = 'propiedad area')
    
    perimetro = property(fget = get_perimetro, doc = 'propiedad perimetro')