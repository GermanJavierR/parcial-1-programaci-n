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

from validaciones import es_entero

"""
1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.
"""

def cargar_matriz_notas(alumnos, cantidad_de_notas):
    """
    Propósito: cargar la matriz con los alumnos dados y la cantidad de notas dadas.
    Parametros: 
        alumnos (int): la cantidad de alumnos que se va a ingresar a la matriz
        canitidad (int): la cantidad de alumnos que se va a cargar a cada alumno.
    return: una matriz cargada con los datos dados.
    """

    if es_entero(alumnos) and es_entero(cantidad_de_notas):
        for i in range(alumnos):
            for j in range(cantidad_de_notas):
                