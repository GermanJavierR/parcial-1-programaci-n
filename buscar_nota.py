"""
4 – Función buscar_nota(): Recibe la matriz y una nota buscada, y
retorna una lista con todas las posiciones (fila, columna) donde aparece
esa nota exacta.
"""

from validaciones import es_entero, es_nota_valida

def buscar_nota(matriz_de_alumnos, nota_a_buscar):
    """
    Propósito: Busca la nota dada en la matriz dada.
    Parametros:
        matriz_de_alumnos (list): matriz de alumnos en la que vamos a buscar la nota dada.
        nota_a_buscar (int): nota que vamos a buscar.
    Return: retorna una lista con todas las posiciones donde aparece la nota ingresada.
    """

    if es_entero(nota_a_buscar) and es_nota_valida(nota_a_buscar):
        nota = int(nota_a_buscar)
        lista_de_posiciones = []
        for i in range(len(matriz_de_alumnos)):
            for j in range(len(matriz_de_alumnos[i])):
                if matriz_de_alumnos[i][j] == nota:
                    lista_de_posiciones += [(i,j)]
        return f"Las posiciones en las que se encuentra la nota ingresa son: {lista_de_posiciones}"
    else:
        return "La nota ingresa no es valida."
