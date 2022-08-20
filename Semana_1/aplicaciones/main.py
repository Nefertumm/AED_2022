# from Semana_1.modulos.circulo_decoradores import Circulo
# from Semana_1.modulos.cuadrado import Cuadrado
# from Semana_1.modulos.punto import Punto
# from Semana_1.modulos.estudiantes import Estudiante
# from Semana_1.modulos.persona import PersonaAleatoria
# from Semana_1.modulos.producto import Producto
# from Semana_1.modulos.calculadoraimc import CalculadoraIMC
# from Semana_1.modulos.analizador import AnalizadorTexto
# from Semana_1.modulos.conversor import ConversorTemperatura

from numbers import Number
import Utils.exceptions as cex

if __name__ == "__main__":
    #template para check básico:
    # check = False
    # while not check:
    #     try:
    #         generic = input('Generic: ')
    #     except ValueError:
    #         print('El tipo de valor no es el correcto')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString, cex.ValueNotNumber) as err:
    #         print(err)
    #     else:
    #         check = True
    #         print('pass')

    # --------------------------------
    # Ejercicio 1

    # check = False
    # while not check:
    #     try:
    #         lado = float(input('Ingrese el lado del cuadrado: '))
    #         c1 = Cuadrado(lado)
    #     except (ValueError, cex.ValueNotNumber):
    #         print('El tipo de valor no es el correcto')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString) as err:
    #         print(err)
    #     else:
    #         check = True
    #         print(c1)

    # --------------------------------
    # Ejercicio 2

    # check = False
    # while not check:
    #     try:
    #         x, y = input('Ingrese x e y separados por coma: ').split(',')
    #         p1 = Punto(float(x), float(y))
    #     except (ValueError, cex.ValueNotNumber):
    #         print('El tipo de valor no es el correcto')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString) as err:
    #         print(err)
    #     else:
    #         check = True
    #         print(p1)

    # --------------------------------
    # Ejercicio 3 y 5

    # p1 = PersonaAleatoria()
    # print(p1.nombre, p1.apellido)

    # --------------------------------
    # Ejercicio 4

    # estudiantesList = []
    # with open('alumnos.txt', 'r') as alumnos:
    #     for alumno in alumnos:
    #         legajo, apellido, nombre, doc, prom = alumno.split(',')
    #         estudiante = Estudiante(legajo, apellido, nombre, doc, prom)
    #         estudiantesList.append(estudiante)
            
    # for estudiante in estudiantesList:
    #     print(f'Estudiante: {estudiante.apellido} {estudiante.nombre} \n Legajo: {estudiante.legajo} \n DNI: {estudiante.documento} \n Promedio: {estudiante.promedio}')
    
    # --------------------------------
    # Ejercicio 6
    
    # check = False
    # while not check:
    #     try:
    #         nombre = input('Ingrese el nombre del producto: ')
    #         precio = float(input('Ingrese el precio: '))
    #         stock = int(input('Ingrese stock del producto: '))
    #         p1 = Producto(nombre, precio, stock)
    #     except ValueError:
    #         print('El precio y el stock deben ser números')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString, cex.ValueNotNumber) as err:
    #         print(err)
    #     else:
    #         check = True
    #         print(p1)

    # --------------------------------
    # Ejercicio 7

    # check = False
    # while not check:
    #     try:
    #         peso = float(input('Ingrese peso: '))
    #         altura = float(input('Ingrese altura: '))
    #     except ValueError:
    #         print('El peso y la altura deben ser números')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString, cex.ValueNotNumber) as err:
    #         print(err)
    #     else:
    #         check = True
    #         imc = CalculadoraIMC(peso, altura)
    #         print(imc)

    # --------------------------------
    # Ejercicio 8

    # check = False
    # while not check:
    #     try:
    #         text = input('Ingrese un texto: ')
    #         analizador = AnalizadorTexto(text)
    #         analizador.depurar_texto()
    #         search_word = input('Ingrese una palabra a buscar: ')
    #         count = analizador.ocurrencia_palabra(search_word)
    #     except (ValueError, cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString, cex.ValueNotNumber) as err:
    #         print(err)
    #     else:
    #         check = True
    #         print(analizador)
    #         print(f'Cantidad de ocurrencias de {search_word}: {count}.')
    
    # --------------------------------
    # Ejercicio 9

    # check = False
    # while not check:
    #     try:
    #         temperatura = float(input('Ingrese una temperatura: '))
    #         desde_unidad = input('Ingrese una unidad: ')
    #         a_unidad = input('Ingrese la unidad a la que quiere convertir: ')
    #         conversor = ConversorTemperatura()
    #         temp_conv = conversor.convertir_a(temperatura, desde_unidad, a_unidad)
    #         print(temp_conv)
    #     except ValueError:
    #         print('La temperatura no es número')
    #     except (cex.ValueBelowZero, cex.ValueEqualsOrBelowZero, cex.ValueEmptyString, cex.ValueNotString, cex.ValueNotNumber) as err:
    #         print(err)
    #     else:
    #         check = True
    
    pass
