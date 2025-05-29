def es_entero(valor):
    if isinstance(valor, int):
        return True
    elif type(valor) == str:
        return valor.isdigit()
    else:
        return False

def es_nota_valida(numero):
    if es_entero(numero):
        return 1 <= numero <= 10
    else:
        return False