
"""
3 – Función mejor_promedio(): Calcula el promedio de cada alumno y
determina cuál tiene el mejor promedio. Retorna el índice del alumno y
el valor del promedio.
"""

from funciones_alumnos import promedio_del_alumno

def mejor_promedio(matriz_de_alumnos):
    """
    Propósito: indicar cual es alumno con mejor promedio de la matriz dada.
    Parametros:
        matriz_de_alumnos (list):  matriz de alumnos de la que se quiere obtener al que tiene mejor promedio.
    Return: Retorna el alumano con el mejor promedio de la matriz de alumnos.
    """
    if matriz_de_alumnos != []:
        alumno_con_mejor_promedio = 0
        for i in range(len(matriz_de_alumnos) - 1):
            if promedio_del_alumno(matriz_de_alumnos[i + 1]) > promedio_del_alumno(matriz_de_alumnos[alumno_con_mejor_promedio]):
                alumno_con_mejor_promedio = i + 1
        print(f"El alumno con mejor promedio es el alumno número {alumno_con_mejor_promedio + 1}")
    else:
        print("La matriz ingresada está vacia.") 


# matriz = [[1,2,3], [10,8,8], [9, 9, 7]]

# mejor_promedio(matriz)