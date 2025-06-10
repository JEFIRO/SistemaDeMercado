import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo INTEGER UNIQUE,
            nome TEXT,
            quantidade INTEGER,
            valor FLOAT,
            categoria TEXT,
            data TEXT
        )"""
        self.cursor.execute(sql)
        self.con.commit()

    def insert(self, produto):
        self.cursor.execute("""
            INSERT INTO produtos (codigo, nome, quantidade, valor, data,categoria)
            VALUES (?, ?, ?, ?, ?,?)
        """, (produto.codigo, produto.nome, produto.quantidade, produto.valor, produto.data, produto.categoria))
        self.con.commit()

    def update(self, id, produto):
        self.cursor.execute("""
            UPDATE produtos SET codigo=?, nome=?, quantidade=?, valor=?, data=?,categoria=? WHERE id=?
        """, (produto.codigo, produto.nome, produto.quantidade, produto.valor, produto.categoria, produto.data, id))
        self.con.commit()

    def updateQTD(self, id, qtd):
        self.cursor.execute("""
            UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?
        """, (qtd, id))
        self.con.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
        self.con.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def findById(self, id):
        self.cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
        return self.cursor.fetchone()
