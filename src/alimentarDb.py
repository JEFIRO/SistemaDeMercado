from CRUD import Database
from src.entity.Produtos import Produtos

db = Database("banco.db")

produtos = [
    Produtos("Detergente", 150, 2.99),
    Produtos("Sabão em pó", 60, 12.49),
    Produtos("Papel higiênico", 100, 9.90),
    Produtos("Desinfetante", 80, 5.49),
    Produtos("Shampoo", 70, 10.99),
    Produtos("Condicionador", 65, 11.49),
    Produtos("Creme dental", 120, 3.99),
    Produtos("Escova de dente", 110, 2.59),
    Produtos("Desodorante", 95, 6.99),
    Produtos("Esponja de aço", 130, 1.49),
    Produtos("Cerveja lata", 200, 3.29),
    Produtos("Refrigerante 2L", 140, 7.79),
    Produtos("Água mineral", 180, 1.89),
    Produtos("Pão de forma", 100, 6.29),
    Produtos("Presunto", 50, 4.79),
    Produtos("Queijo mussarela", 50, 6.99),
    Produtos("Margarina", 75, 4.49),
    Produtos("Iogurte", 90, 3.29),
    Produtos("Frango congelado", 40, 15.99),
    Produtos("Carne moída", 35, 18.49)
]


for p in produtos:
    db.insert(p)
