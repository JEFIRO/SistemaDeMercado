from random import randint
from tkinter import *
from tkinter import ttk


class Estoque:
    def __init__(self):
        self.gerarCodigo()
        self.tela()

    def tela(self):
        janela = Tk()
        janela.title("Estoque")
        janela.state('zoomed')
        janela.resizable(False, False)
        menuBarra = Menu(janela)

        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Novo")
        menuArquivo.add_command(label="Abrir")
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=janela.quit)
        menuBarra.add_cascade(label="Arquivo", menu=menuArquivo)

        janela.config(menu=menuBarra)

        framePrincipal = Frame(janela, bg="blue")
        framePrincipal.pack(fill=BOTH, expand=True)

        frameCadastro = Frame(framePrincipal, bg="red", width=400)
        frameCadastro.pack(side=LEFT, fill=Y)

        labelProduto = Label(frameCadastro, text="Nome do produto")
        labelProduto.grid(row=0, column=0, padx=5, pady=5)

        entryProduto = Entry(frameCadastro)
        entryProduto.grid(row=0, column=1, padx=5, pady=5)

        labelQtd = Label(frameCadastro, text="Quantidade")
        labelQtd.grid(row=1, column=0, padx=5, pady=5)

        entryQtd = Entry(frameCadastro)
        entryQtd.grid(row=1, column=1, padx=5, pady=5)

        labelValor = Label(frameCadastro, text="Valor")
        labelValor.grid(row=2, column=0, padx=5, pady=5)

        entryValor = Entry(frameCadastro)
        entryValor.grid(row=2, column=1, padx=5, pady=5)

        frameTopo = Frame(framePrincipal, bg='brown')
        frameTopo.pack(fill=BOTH, expand=True, side=TOP)

        labelTitulo = Label(frameTopo, text="Pesquisa de produtos", font=("Arial", 16), bg='brown', fg='white')
        labelTitulo.pack(fill=X, side=TOP)

        framePesquisa = Frame(frameTopo, bg='brown')
        framePesquisa.pack(fill=BOTH, expand=True, side=TOP)

        labelPesquisa = Label(framePesquisa, text="Nome", font=("Arial", 12), bg='brown', fg='white')
        labelPesquisa.pack(fill=X, side=LEFT, padx=5)

        entryPesquisa = Entry(framePesquisa, width=30)
        entryPesquisa.pack(fill=X, side=LEFT, padx=5)

        buttonPesquisa = Button(framePesquisa, text="Buscar")
        buttonPesquisa.pack(fill=X, side=LEFT, padx=5)

        frameFiltro = Frame(frameTopo, bg='green')
        frameFiltro.pack(fill=BOTH, expand=True, side=BOTTOM)

        labelPesquisa = Label(frameFiltro, text="Filtrar por: ", font=("Arial", 12), bg='brown', fg='white')
        labelPesquisa.pack(fill=X, side=LEFT, padx=5)

        comboFiltro = ttk.Combobox(frameFiltro, width=12, state="readonly")
        comboFiltro["values"] = ("Nome", "Quantidade", "preço")
        comboFiltro.current(0)
        comboFiltro.pack(fill=X, side=LEFT, padx=5)

        comboButton = Button(frameFiltro, text="Filtrar")
        comboButton.pack(fill=X, side=LEFT, padx=5)

        frameCentral = Frame(framePrincipal, bg='yellow')
        frameCentral.pack(fill=BOTH, expand=True)

        colunas = ("Codigo", "Produto", "Qtd", "Preço")
        tree = ttk.Treeview(frameCentral, columns=colunas, show="headings", height=10)
        tree.pack(padx=10, pady=10, fill=BOTH, expand=True, side=BOTTOM)

        # Cabeçalhos
        tree.heading("Codigo", text="Codigo")
        tree.heading("Produto", text="Produto")
        tree.heading("Qtd", text="Qtd")
        tree.heading("Preço", text="Preço")

        # Tamanhos das colunas

        tree.column("Codigo", width=150)
        tree.column("Produto", width=150)
        tree.column("Qtd", width=10)
        tree.column("Preço", width=80)

        # Dados de exemplo
        produtos = [
            ("243235342356", "Arroz", 2, "R$ 10,00"),
            ("243235342356", "Macarrão", 3, "R$ 5,50"),
            ("243235342356", "Feijão", 1, "R$ 8,00")
        ]

        for item in produtos:
            tree.insert("", END, values=item)

        janela.mainloop()

    def gerarCodigo(self):
        code = ''
        for _ in range(6):
            pin = randint(0, 9)
            code += str(pin)
        return code


if __name__ == "__main__":
    Estoque()
