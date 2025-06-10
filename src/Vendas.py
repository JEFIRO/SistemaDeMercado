import sqlite3


class Vendas:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT,
                quantidade INTEGER,
                preco REAL,
                forma_de_pagamento TEXT,
                categoria TEXT,
                data TEXT
            )
        """)
        self.con.commit()

    def registrarVenda(self, produto, quantidade, preco, categoria, formaDePagamento, data):
        self.cursor.execute("""
            INSERT INTO vendas (produto, quantidade, preco, categoria, forma_de_pagamento, data)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (produto, quantidade, preco, categoria, formaDePagamento, data))
        self.con.commit()

    def relatorioPorDia(self):
        self.cursor.execute("""
            SELECT data, SUM(quantidade * preco) AS total
            FROM vendas
            GROUP BY data
            ORDER BY data DESC
        """)
        return self.cursor.fetchall()

    def relatorioPorProduto(self):
        self.cursor.execute("""
            SELECT produto, SUM(quantidade), SUM(quantidade * preco)
            FROM vendas
            GROUP BY produto
            ORDER BY SUM(quantidade * preco) DESC
        """)
        return self.cursor.fetchall()

    def relatorioPorFormaDePagamento(self):
        self.cursor.execute("""
            SELECT forma_de_pagamento, SUM(quantidade * preco) AS total
            FROM vendas
            GROUP BY forma_de_pagamento
        """)
        return self.cursor.fetchall()

    def relatorioDetalhado(self):
        self.cursor.execute("""
            SELECT data, produto, quantidade, preco, categoria, forma_de_pagamento
            FROM vendas
            ORDER BY data DESC
        """)
        return self.cursor.fetchall()

    def relatorioPorCategoria(self):
        self.cursor.execute("""
            SELECT categoria, SUM(quantidade), SUM(quantidade * preco) AS total
            FROM vendas
            GROUP BY categoria
            ORDER BY total DESC
        """)
        return self.cursor.fetchall()

    def relatorioGeral(self):
        self.cursor.execute("""
            SELECT SUM(quantidade), SUM(quantidade * preco)
            FROM vendas
        """)
        return self.cursor.fetchone()
