def es_entero(valor):
    if isinstance(valor, int):
        return True
    elif type(valor) == str:
        return valor.isdigit()


def s_nota_valida(numero):
    return 1 <= numero <= 10