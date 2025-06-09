from datetime import date
from random import randint


def gerar_codigo():
    codigo = str(randint(1, 9)) + ''.join(str(randint(0, 9)) for _ in range(5))
    return codigo


class Produtos:

    def __init__(self, nome, quantidade, valor, codigo=None, data=None):
        self.codigo = codigo if codigo is not None else gerar_codigo()
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.data = data if data is not None else date.today().strftime("%Y-%m-%d")
