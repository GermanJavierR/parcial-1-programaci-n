"""
PARTE 2 – EJERCICIO PRÁCTICO
Contexto: Una institución educativa necesita registrar las notas de sus
alumnos en distintos exámenes. Cada fila de una matriz representa un
alumno y cada columna un examen.
Requisitos Generales para Todos los Puntos:
- Se deben modularizar todas las operaciones. No se permite resolver
todo en el main.
- No está permitido el uso de funciones propias de Python como max,
min, sum, enumerate, etc.
- La validación debe hacerse en la función de carga, verificando que
cada nota sea un número entero entre 1 y 10.
- Se debe implementar un menú con opciones para ejecutar cada punto
de forma separada.
- Usar estructuras adecuadas, acumuladores, contadores y recorrido
doble.
- Nombrar las funciones tal como se indican a continuación.
"""

from parametros_de_la_matriz import ingresar_valor_valido
from cargar_matriz_de_notas import cargar_matriz_notas
from porcentaje_de_aprobados import porcentaje_aprobados
from mejor_promedio import mejor_promedio
from buscar_nota import buscar_nota

alumnos = ingresar_valor_valido()
examenes = ingresar_valor_valido()

matriz_alumnos = [[0 for n in range(examenes)] for a in range(alumnos)]

def menu(matriz): # ingreso la matriz que con la que voy a operar.
    """
    Propósito: indicarle al usuario cuales son las acciones que puede ejecutar.
    Return: valor de lo que ingreso el usuario.
    """
    print("Bienvenido, las operación que puede realizar son: ")
    print("1. Cargar la matriz de alumnos.")
    print("2. Mostrar el porcentaje de aprobación de cada alumno.")
    print("3. Mostrar el alumno con mejor promedio.")
    print("4. Buscar las ubicaciones donde aparece una nota en especifica.")
    continuar = "si"
    while continuar != "no":
        opcion_a_realizar = input("Por favor, ingrese el número de la operación que desee realizar: ")
        match opcion_a_realizar:
            case "1":
                matriz = cargar_matriz_notas(alumnos, examenes)
                continuar = input("Desea realizar otra operación? 'Si/No': ").lower()
            case "2":
                porcentaje_aprobados(matriz)
                continuar = input("Desea realizar otra operación? 'Si/No': ").lower()
            case "3":
                mejor_promedio(matriz)
                continuar = input("Desea realizar otra operación? 'Si/No': ").lower()
            case "4":
                nota_a_buscar = input("Por favor, ingrese la nota que desea buscar: ")
                print(buscar_nota(matriz, nota_a_buscar))
                continuar = input("Desea realizar otra operación? 'Si/No': ").lower()
            case _:
                print("El valor ingresado no corresponde algunas de las opciones validas.")
                continuar = input("Desea realizar otra operación? 'Si/No': ").lower()


menu(matriz_alumnos)