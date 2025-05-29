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

from validaciones import es_entero, es_nota_valida

"""
1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.
"""


alumnos = 3
examenes = 6

matriz_alumnos = [[0 for a in range(examenes)] for c in range(alumnos)]



def cargar_matriz_notas(cantidad_de_alumnos, cantidad_de_notas):
    """
    Propósito: cargar la matriz con los alumnos dados y la cantidad de notas dadas.
    Parametros: 
        alumnos (int): la cantidad de alumnos que se va a ingresar a la matriz
        canitidad (int): la cantidad de alumnos que se va a cargar a cada alumno.
    return: una matriz cargada con los datos dados.
    """

    if es_entero(cantidad_de_alumnos) and es_entero(cantidad_de_notas): # Valido si ambos numero ingresado son número enteros

        for i in range(cantidad_de_alumnos):  # Recorro la cantidad de alumnos que tengo.
            for j in range(cantidad_de_notas): # Recorro cada nota que tiene el alumno.
                nota_del_alumnos = input(f"Por favor, ingrese la nota del examen número {j + 1} alumno {i + 1}: ")
                while not es_entero(nota_del_alumnos) and not es_nota_valida(nota_del_alumnos):  # si la nota ingresado no es valida, dice que no a ingresado una nota valida.
                    print("La nota ingresada no es valida.")
                    nota_del_alumnos = input(f"Por favor, ingrese la nota del examen número {j + 1} alumnos: ")
                nota_del_alumnos = int(nota_del_alumnos) # el usuario ingresa la nota del alumno.
                matriz_alumnos[i][j] = nota_del_alumnos # le asigno la la nota correspondiente al alumnno.

        print(matriz_alumnos) # Imprimo la matriz de con los valores ingresados


cargar_matriz_notas(alumnos,examenes)

# filas = 3
# columnas = 6

# matriz_alumnos = [[0 for a in range(columnas)] for c in range(filas)]
# print(matriz_alumnos)

"""
2 – Función porcentaje_aprobados(): Calcula el porcentaje de
exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
individual. Usar contadores y acumuladores.
"""

def porcentaje_aprobados(matriz_de_alumnos):
    """
    Propósito: indicar cual es el porcentaje de examenes aprobados que tiene cada alumno.
    Parametros:
        matriz_de_alumnos (list): matriz de alumnos que se va a procesar
    Return: retorna un resumen de cada alumno con la cantidad de notas aprobadas y el porcentaje de aprobados que tiene.
    """

    for i in range(len(matriz_de_alumnos)): # Recorro tantas veces como la cantidad de alumnos que tengo
        examenes_totales = len(matriz_de_alumnos[i]) # Establesco la canitdad total de examenes del alumno
        examenes_aprobados = 0 # inicializo la variable de la cantidad examenes que aprobo el alumno
        for j in matriz_de_alumnos[i]:
            if j >= 6: # Verifico si la nota actual es aprobada o no.
                examenes_aprobados += 1 # Si está aprobado entonces suma uno.
        porcentaje_de_aprobadas_del_alumno = round(examenes_aprobados * 100 / examenes_totales, 2) # realizo la operación para sacar el porcentaje 
        print(f"El alumno {i + 1} aprobo {examenes_aprobados}, su porcentaje de aprobados es de {porcentaje_de_aprobadas_del_alumno}%") #Doy la descripción del alumno. 


porcentaje_aprobados(matriz_alumnos)