from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.tela()

    def tela(self):
        # Paleta de cores
        self.azul_marinho = "#001F3F"
        self.azul_medio = "#4682B4"
        self.amarelo_mostarda = "#FFDB58"
        self.branco_claro = "#F5FFFA"
        self.texto_claro = "#FAFAFA"

        self.janela = Tk()
        self.janela.title("Tela Maximizando")
        self.janela.state('zoomed')
        self.janela.resizable(False, False)

        def puxarTelaDeEstoque():
            from estoque import Estoque
            self.janela.destroy()
            Estoque()

        menuBarra = Menu(self.janela)
        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Estoque", command=puxarTelaDeEstoque)
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=self.janela.quit)
        menuBarra.add_cascade(label="Menu", menu=menuArquivo)
        self.janela.config(menu=menuBarra)

        # Frame principal
        self.framePrincipal = Frame(self.janela, bg=self.azul_marinho)
        self.framePrincipal.pack(expand=True, fill=BOTH)

        # Lateral esquerda
        self.frameLateral = Frame(self.framePrincipal, bg=self.azul_medio, width=400)
        self.frameLateral.pack(side=LEFT, fill=Y)

        def criar_label_lateral(texto, negrito=False):
            font_style = ("Arial", 18, "bold") if negrito else ("Arial", 18)
            return Label(self.frameLateral, text=texto, font=font_style,
                         fg=self.branco_claro, bg=self.azul_marinho)

        criar_label_lateral("Valor Da Compra", True).pack(fill=X, pady=5, padx=5)
        criar_label_lateral("00.00").pack(fill=X, pady=10, padx=5)
        criar_label_lateral("Desconto", True).pack(fill=X, pady=10, padx=5)
        criar_label_lateral("0").pack(fill=X, pady=10, padx=5)
        criar_label_lateral("Valor Total", True).pack(fill=X, pady=10, padx=5)
        criar_label_lateral("00.00").pack(fill=X, pady=10, padx=5)

        # Separador visual
        self.saparete = Frame(self.framePrincipal, bg=self.branco_claro, width=2)
        self.saparete.pack(side=LEFT, fill=Y)

        # Frame à direita
        self.frameDireita = Frame(self.framePrincipal, bg=self.azul_medio)
        self.frameDireita.pack(side=LEFT, fill=BOTH, expand=True)

        self.frameCentral = Frame(self.frameDireita, bg=self.azul_medio, height=400)
        self.frameCentral.pack(side=TOP, fill=BOTH, expand=True)

        colunas = ("Codigo", "Produto", "Qtd", "Preço")
        self.tree = ttk.Treeview(self.frameCentral, columns=colunas, show="headings", height=10)
        self.tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Cabeçalhos
        for col in colunas:
            self.tree.heading(col, text=col)
        self.tree.column("Codigo", width=150)
        self.tree.column("Produto", width=150)
        self.tree.column("Qtd", width=10)
        self.tree.column("Preço", width=80)

        # Estilização da Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background=self.branco_claro,
                        foreground="black",
                        rowheight=25,
                        fieldbackground=self.branco_claro)
        style.map("Treeview", background=[("selected", self.amarelo_mostarda)])

        produtos = [
            ("243235342356", "Arroz", 2, "R$ 10,00"),
            ("243235342356", "Feijão", 1, "R$ 8,00"),
            ("243235342356", "Macarrão", 3, "R$ 5,50"),
        ]
        for item in produtos:
            self.tree.insert("", END, values=item)

        # Rodapé com entrada de dados
        self.frameInferior = Frame(self.frameDireita, bg=self.azul_marinho, height=200)
        self.frameInferior.pack(side=BOTTOM, fill=X)

        labelCodigo = Label(self.frameInferior, text="Código", bg=self.azul_marinho,
                            fg=self.texto_claro, font=("Arial", 14))
        labelCodigo.grid(row=0, column=0, pady=10, padx=5)

        entryCodigo = Entry(self.frameInferior, width=15)
        entryCodigo.grid(row=0, column=1, pady=10, padx=5)

        labelQtd = Label(self.frameInferior, text="Qtd", bg=self.azul_marinho,
                         fg=self.texto_claro, font=("Arial", 14))
        labelQtd.grid(row=0, column=2, pady=10, padx=5)

        entryQtd = Entry(self.frameInferior, width=15)
        entryQtd.grid(row=0, column=3, pady=10, padx=5)

        self.janela.mainloop()


if __name__ == "__main__":
    Main()
