# from modulos.circulo_decoradores import Circulo
# from modulos.estudiantes import Estudiante
# from modulos.persona import PersonaAleatoria
# from modulos.producto import Producto
from modulos.calculadoraimc import CalculadoraIMC
# from modulos.analizador import AnalizadorTexto
from modulos.conversor import ConversorTemperatura

if __name__ == "__main__":
    # p1 = PersonaAleatoria()
    # print(p1.nombre, p1.apellido)
    
    # c1 = Circulo(5)
    # print(c1.radio)
    
    # print(c1.area)
    # print(c1.perimetro)
    
    # alumnosList = []
    # with open('alumnos.txt', 'r') as alumnos:
    #     for alumno in alumnos:
    #         legajo, apellido, nombre, doc, prom = alumno.split(',')
    #         estudiante = Estudiante(legajo, apellido, nombre, doc, prom)
    #         alumnosList.append(estudiante)
            
    # for alumno in alumnosList:
    #     print(f'Alumno: {alumno.apellido} {alumno.nombre} \n Legajo: {alumno.legajo} \n DNI: {alumno.documento} \n Promedio: {alumno.promedio}')
    
    # est = Estudiante('kjf', 'Hola', 'Mundo', 123123123, 5.4)
    # print(est)
    
    # p1 = Producto('Hola', 0.5, 12)
    # print(p1)
    # p1.aplicar_descuento(50)
    # print(p1)
    
    check = False
    while not check:
        try:
            peso = float(input('Ingrese peso: '))
            altura = float(input('Ingrese altura: '))
        except ValueError as e:
            print(e)
        else:
            check = True
            imc = CalculadoraIMC(peso, altura)
            print(imc)

    # analizador_texto = AnalizadorTexto('Hola como  :__  va l a banda')
    # print(analizador_texto)
    # analizador_texto.depurar_texto()
    # print(analizador_texto)
    
    # check = False
    # while not check:
    #     try:
    #         temperatura = float(input('Ingrese una temperatura: '))
    #         desde_unidad = input('Ingrese una unidad: ')
    #         a_unidad = input('Ingrese la unidad a la que quiere convertir: ')
    #         conversor = ConversorTemperatura()
    #         temp_conv = conversor.convertir_a(temperatura, desde_unidad, a_unidad)
    #         print(temp_conv)
    #     except ValueError as e:
    #         print(e)
    #     else:
    #         check = True
            
            