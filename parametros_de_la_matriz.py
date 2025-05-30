"""
Verifica si los valores para los alumnos y la cantidad de notas es valido.
"""

from validaciones import es_entero

def ingresar_valor_valido():
    """
    
    """
    valor = input("Antes de empezar por favor ingrese la canitdad de alumnos que tenda la matriz: ")

    while not es_entero(valor):
        print("El valor ingresado no es valido.")
        valor = input("Antes de empezar por favor ingrese la canitdad de alumnos que tenda la matriz: ")

    valor = int(valor)
    
    return valor
