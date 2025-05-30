def es_entero(valor):
    if isinstance(valor, int):
        return True
    elif type(valor) == str:
        return valor.isdigit()
    else:
        return False


def es_nota_valida(numero):
    if es_entero(numero):
        valor = int(numero)
        return 1 <= valor <= 10


def es_una_lista(valor):
    if type(valor) == list:
        return True
    else:
        return False 