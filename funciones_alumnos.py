from validaciones import es_una_lista, es_entero

def promedio_del_alumno(alumno):
    """
    Propósito: Indicar el promedio del alumno dado.
    Parametro:
        alumno (list): lista de notas del alumno.
    Return: retorna el promedio del alumno.
    """
    if es_una_lista(alumno): # Verifico si la lista de notas ingresada no es vacía.
        cantidad_de_notas = 0 # Inicializo la variable que va a tener la cantidad de notas del alumno.
        suma_de_las_notas = 0 # Inicializo la variable que va a tener la suma total de todas las notas.
        for i in alumno: # Para cada nota del alumno ejecuto lo siguiente:
            if es_entero(i): # Si la nota es un entero hace lo siguiente:
                suma_de_las_notas += i # Se le suma la nota a la variable suma_de_todas_las_notas
                cantidad_de_notas += 1 # Se le suma uno a la variable canitdad_de_notas.
        promedio = suma_de_las_notas / cantidad_de_notas # Calcula el promedio con las dos variables que tengo.
        return promedio # Retorno el promedio del alumno.

