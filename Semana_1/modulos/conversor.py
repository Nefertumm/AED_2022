class ConversorTemperatura:
    def __init__(self) -> None:
        pass
    
    def __convertir_a_kelvin(self, temp: float, uni: str) -> float:
        """Convertimos la temperatura a kelvin"""
        if uni == 'K':
            return temp
        elif uni == 'C':
            return temp + 273.15
        else:
            return (temp + 459.67) * (5/9)
        
    def __convertir_a_celsius(self, temp_k: float) -> float:
        """Convertimos la temperatura a celsius (desde K)"""
        temp_en_c = temp_k - 273.15
        return temp_en_c
    
    def __convertir_a_fahrenheit(self, temp_k: float) -> float:
        """Convertimos la temperatura a fahrenheit"""
        return temp_k * (9/5) - 459.67
        
    def convertir_a(self, temperatura: float, desde_unidad: str, a_unidad: str) -> float:
        """Convierte la temperatura desde una unidad a otra"""
        desde_unidad = desde_unidad.upper().strip()
        a_unidad = a_unidad.upper().strip()
        
        unidades = ['C', 'K', 'F']
        
        if (temperatura < 0 and desde_unidad == 'K'):
            raise ValueError('La temperatura se encuentra por debajo del cero absoluto.')
        if not desde_unidad in unidades:
            raise ValueError('La unidad de entrada no es correcta')
        if not a_unidad in unidades:
            raise ValueError('La unidad de salida no es correcta')
        
        if (desde_unidad == a_unidad):
            return temperatura
        else:
            temp_k = self.__convertir_a_kelvin(temperatura, desde_unidad)
            if a_unidad == 'K':
                return temp_k
            elif a_unidad == 'C':
                return self.__convertir_a_celsius(temp_k)
            else:
                return self.__convertir_a_fahrenheit(temp_k)
        
