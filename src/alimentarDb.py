from CRUD import Database
from src.entity.Produtos import Produtos

db = Database("banco.db")

produtos = [
    Produtos("Detergente", 150, 2.99, "Limpeza"),
    Produtos("Sabão em pó", 60, 12.49, "Limpeza"),
    Produtos("Papel higiênico", 100, 9.90, "Higiene"),
    Produtos("Desinfetante", 80, 5.49, "Limpeza"),
    Produtos("Shampoo", 70, 10.99, "Higiene"),
    Produtos("Condicionador", 65, 11.49, "Higiene"),
    Produtos("Creme dental", 120, 3.99, "Higiene"),
    Produtos("Escova de dente", 110, 2.59, "Higiene"),
    Produtos("Desodorante", 95, 6.99, "Higiene"),
    Produtos("Esponja de aço", 130, 1.49, "Limpeza"),
    Produtos("Cerveja lata", 200, 3.29, "Bebidas"),
    Produtos("Refrigerante 2L", 140, 7.79, "Bebidas"),
    Produtos("Água mineral", 180, 1.89, "Bebidas"),
    Produtos("Pão de forma", 100, 6.29, "Alimentos"),
    Produtos("Presunto", 50, 4.79, "Alimentos"),
    Produtos("Queijo mussarela", 50, 6.99, "Alimentos"),
    Produtos("Margarina", 75, 4.49, "Alimentos"),
    Produtos("Iogurte", 90, 3.29, "Alimentos"),
    Produtos("Frango congelado", 40, 15.99, "Alimentos"),
    Produtos("Carne moída", 35, 18.49, "Alimentos")
]
produtos += [
    Produtos("Arroz 5kg", 60, 22.90, "Alimentos"),
    Produtos("Feijão 1kg", 70, 7.49, "Alimentos"),
    Produtos("Açúcar 1kg", 90, 3.59, "Alimentos"),
    Produtos("Café 500g", 85, 17.90, "Alimentos"),
    Produtos("Sal 1kg", 100, 2.49, "Alimentos"),
    Produtos("Óleo de soja 900ml", 80, 6.99, "Alimentos"),
    Produtos("Farinha de trigo 1kg", 65, 4.89, "Alimentos"),
    Produtos("Achocolatado 400g", 50, 5.79, "Alimentos"),
    Produtos("Molho de tomate", 90, 2.99, "Alimentos"),
    Produtos("Macarrão 500g", 100, 3.49, "Alimentos"),

    Produtos("Sabonete", 150, 1.99, "Higiene"),
    Produtos("Fio dental", 60, 3.29, "Higiene"),
    Produtos("Absorvente", 70, 8.49, "Higiene"),
    Produtos("Lenço umedecido", 55, 6.29, "Higiene"),
    Produtos("Álcool em gel", 40, 4.99, "Higiene"),

    Produtos("Amaciante", 70, 7.99, "Limpeza"),
    Produtos("Água sanitária", 100, 3.49, "Limpeza"),
    Produtos("Multiuso", 90, 6.29, "Limpeza"),
    Produtos("Lustra-móveis", 50, 9.79, "Limpeza"),
    Produtos("Pano de chão", 80, 2.89, "Limpeza"),

    Produtos("Suco de caixinha", 120, 3.79, "Bebidas"),
    Produtos("Energético", 45, 7.99, "Bebidas"),
    Produtos("Leite longa vida", 150, 4.69, "Bebidas"),

    Produtos("Pilha AA", 40, 6.99, "Outros"),
    Produtos("Velas", 30, 2.49, "Outros"),
    Produtos("Fósforos", 80, 1.29, "Outros"),
    Produtos("Saco de lixo 30L", 100, 5.49, "Outros"),
    Produtos("Filtro de papel", 60, 3.19, "Outros")
]


for p in produtos:
    db.insert(p)
