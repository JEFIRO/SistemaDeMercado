from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.tela()

    def tela(self):
        self.azulmarinho = "#0e0941"
        self.janela = Tk()
        self.janela.title("Tela Maximizando")
        self.janela.state('zoomed')
        self.janela.resizable(False, False)

        menuBarra = Menu(self.janela)

        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Novo")
        menuArquivo.add_command(label="Abrir")
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=self.janela.quit)
        menuBarra.add_cascade(label="Arquivo", menu=menuArquivo)

        self.janela.config(menu=menuBarra)


        self.framePrincipal = Frame(self.janela, bg=self.azulmarinho)
        self.framePrincipal.pack(expand=True, fill=BOTH)

        # Lateral fixo
        self.frameLateral = Frame(self.framePrincipal, bg='red', width=400)
        self.frameLateral.pack(side=LEFT, fill=Y)

        labelTitulo = Label(self.frameLateral, text="Valor Da Compra", font=("Arial", 18))
        labelTitulo.grid(row=0, column=0, columnspan=5, pady=5)

        labelValor = Label(self.frameLateral, text="160,00", font=("Arial", 18))
        labelValor.grid(row=1, column=0, columnspan=5, pady=5)

        labelDescontoTitulo = Label(self.frameLateral, text="Desconto", font=("Arial", 18))
        labelDescontoTitulo.grid(row=2, column=0, columnspan=5, pady=5)

        labelDescontoValor = Label(self.frameLateral, text="12", font=("Arial", 18))
        labelDescontoValor.grid(row=3, column=0, columnspan=5, pady=5)

        labelTotalTitulo = Label(self.frameLateral, text="Valor Total", font=("Arial", 18))
        labelTotalTitulo.grid(row=4, column=0, columnspan=5, pady=5)

        labelTotalValor = Label(self.frameLateral, text="148,00", font=("Arial", 18))
        labelTotalValor.grid(row=5, column=0, columnspan=5, pady=5)

        # Frame à direita que ocupa o resto do espaço
        self.frameDireita = Frame(self.framePrincipal, bg='blue')
        self.frameDireita.pack(side=LEFT, fill=BOTH, expand=True)

        self.frameCentral = Frame(self.frameDireita, bg='yellow', height=400)
        self.frameCentral.pack(side=TOP, fill=BOTH, expand=True)

        colunas = ("Codigo", "Produto", "Qtd", "Preço")
        self.tree = ttk.Treeview(self.frameCentral, columns=colunas, show="headings", height=10)
        self.tree.pack(padx=10, pady=10,fill=X)

        # Cabeçalhos
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Qtd", text="Qtd")
        self.tree.heading("Preço", text="Preço")

        # Tamanhos das colunas

        self.tree.column("Codigo", width=150)
        self.tree.column("Produto", width=150)
        self.tree.column("Qtd", width=10)
        self.tree.column("Preço", width=80)

        # Dados de exemplo
        produtos = [
            ("243235342356", "Arroz", 2, "R$ 10,00"),
            ("243235342356", "Feijão", 1, "R$ 8,00"),
            ("243235342356", "Macarrão", 3, "R$ 5,50"),
        ]

        for item in produtos:
            self.tree.insert("", END, values=item)

        self.frameInferior = Frame(self.frameDireita, bg='green', height=200)
        self.frameInferior.pack(side=BOTTOM, fill=X)

        labelCodigo = Label(self.frameInferior, text="Codigo")
        labelCodigo.grid(row=0, column=0, pady=5)

        entryCodigo = Entry(self.frameInferior, width=15)
        entryCodigo.grid(row=0, column=1, pady=5, padx=5)

        labelQtd = Label(self.frameInferior, text="Qtd")
        labelQtd.grid(row=0, column=2, pady=5, padx=5)

        entryQtd = Entry(self.frameInferior, width=15)
        entryQtd.grid(row=0, column=3, pady=5, padx=5)

        self.janela.mainloop()



if __name__ == "__main__":
    Main()
