from datetime import date
from random import randint


def gerar_codigo():
    codigo = str(randint(1, 9)) + ''.join(str(randint(0, 9)) for _ in range(7))
    return codigo


class Produtos:

    def __init__(self, nome, quantidade, valor, categoria, codigo=None, data=None, id=None):
        self.id = id
        self.codigo = codigo if codigo is not None else gerar_codigo()
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.categoria = categoria
        self.data = data if data is not None else date.today().strftime("%Y-%m-%d")

    def __str__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', quantidade={self.quantidade}, valor={self.valor}, codigo={self.codigo}, data='{self.data}')"
