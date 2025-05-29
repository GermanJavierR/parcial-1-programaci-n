from validaciones import es_una_lista, es_entero

def promedio_del_alumno(alumno):
    """
    Propósito: Indicar el promedio del alumno dado.
    Parametro:
        alumno (list): lista de notas del alumno.
    Return: retorna el promedio del alumno.
    """
    if es_una_lista(alumno):
        cantidad_de_notas = 0
        suma_de_las_notas = 0
        for i in alumno:
            if es_entero(i):
                suma_de_las_notas += i
                cantidad_de_notas += 1
