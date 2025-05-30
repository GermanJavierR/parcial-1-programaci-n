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