"""
1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.
"""

from validaciones import es_entero, es_nota_valida


def cargar_matriz_notas(cantidad_de_alumnos = 0, cantidad_de_notas = 0):
    """
    Propósito: cargar la matriz con los alumnos dados y la cantidad de notas dadas.
    Parametros: 
        alumnos (int): la cantidad de alumnos que se va a ingresar a la matriz
        canitidad (int): la cantidad de alumnos que se va a cargar a cada alumno.
    return: una matriz cargada con los datos dados.
    """

    if es_entero(cantidad_de_alumnos) and es_entero(cantidad_de_notas): # Valido si ambos numero ingresado son número enteros

        matriz_alumnos = [[0 for a in range(cantidad_de_notas)] for c in range(cantidad_de_alumnos)]

        for i in range(cantidad_de_alumnos):  # Recorro la cantidad de alumnos que tengo.
            for j in range(cantidad_de_notas): # Recorro cada nota que tiene el alumno.
                nota_del_alumnos = input(f"Por favor, ingrese la nota del examen número {j + 1} alumno {i + 1}: ")
                while not es_entero(nota_del_alumnos) or not es_nota_valida(nota_del_alumnos): # Verifica si valor ingresado en nota_del_alumno es entero y valido.
                    print("El valor ingresado no es valido.")
                    nota_del_alumnos = input(f"Por favor, ingrese la nota del examen número {j + 1} alumnos {i + 1}: ")
                nota_del_alumnos = int(nota_del_alumnos) # se guarda la nota ingresada como un int.
                matriz_alumnos[i][j] = nota_del_alumnos # le asigno la la nota correspondiente al alumnno.

        return matriz_alumnos # retorno la matriz de los alumnos con los valores ingresados