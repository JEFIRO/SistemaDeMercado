from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from CRUD import Database
from entity.Produtos import Produtos


class Estoque:
    def __init__(self):
        self.produtos = None
        self.itemSelecionado = None

        self.azulMarinho = "#001F3F"
        self.azulMedio = "#4682B4"
        self.amareloMostarda = "#FFDB58"
        self.brancoClaro = "#F5FFFA"
        self.textoClaro = "#FAFAFA"

        self.tela()

    def tela(self):
        db = Database("banco.db")
        janela = Tk()
        janela.title("Estoque")
        janela.state('zoomed')
        janela.resizable(False, False)

        def puxarTelaDeVendas():
            from main import Main
            janela.destroy()
            Main()

        menuBarra = Menu(janela)

        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Vendas", command=puxarTelaDeVendas)
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=janela.quit)
        menuBarra.add_cascade(label="Menu", menu=menuArquivo)

        janela.config(menu=menuBarra)

        framePrincipal = Frame(janela, bg="blue")
        framePrincipal.pack(fill=BOTH, expand=True)

        frameCadastro = Frame(framePrincipal, bg=self.azulMarinho, width=400)
        frameCadastro.pack(side=LEFT, fill=Y)

        labelProduto = Label(frameCadastro, text="Nome do produto", bg=self.azulMarinho, font=("Arial", 16),
                             fg=self.brancoClaro)
        labelProduto.grid(row=0, column=0, padx=5, pady=5)

        entryProduto = Entry(frameCadastro)
        entryProduto.grid(row=0, column=1, padx=5, pady=5)

        labelQtd = Label(frameCadastro, text="Quantidade", bg=self.azulMarinho, font=("Arial", 16), fg=self.brancoClaro)
        labelQtd.grid(row=1, column=0, padx=5, pady=5)

        entryQtd = Entry(frameCadastro)
        entryQtd.grid(row=1, column=1, padx=5, pady=5)

        labelValor = Label(frameCadastro, text="Valor", bg=self.azulMarinho, font=("Arial", 16), fg=self.brancoClaro)
        labelValor.grid(row=2, column=0, padx=5, pady=5)

        entryValor = Entry(frameCadastro)
        entryValor.grid(row=2, column=1, padx=5, pady=5)

        labelCategoria = Label(frameCadastro, text="Categoria", bg=self.azulMarinho, font=("Arial", 16),
                               fg=self.brancoClaro)
        labelCategoria.grid(row=3, column=0, padx=5, pady=5)

        comboCategoria = ttk.Combobox(frameCadastro, width=17, state="readonly")
        comboCategoria["values"] = ("Outros", "Alimentos", "Limpeza", "Higiene", "Bebidas")
        comboCategoria.current(0)
        comboCategoria.grid(row=3, column=1, padx=5, pady=5)

        def limparEntry():
            comboCategoria.current(0)
            entryProduto.delete(0, END)
            entryQtd.delete(0, END)
            entryValor.delete(0, END)

        def cadastrarItem():
            if entryProduto.get() == "" or entryQtd.get() == "" or entryValor.get() == "" or comboCategoria.get() == "":
                return messagebox.showerror("Erro", "Todos os Campos devem ser preenchidos!")
            try:
                quantidade = int(entryQtd.get())
                valor = float(entryValor.get().replace(",", "."))

                produto = Produtos(entryProduto.get().capitalize(), quantidade, valor, comboCategoria.get())
                db.insert(produto)
                preencherList()
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                limparEntry()

            except ValueError:
                messagebox.showerror("Erro", "Quantidade e valor devem ser números.")
            except Exception as e:
                messagebox.showerror("Erro inesperado", f"Ocorreu um erro:\n{e}")


        buttonCadastrar = Button(frameCadastro, text="cadastrar item", width=40, command=cadastrarItem)
        buttonCadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        def atualizarItem():
            if self.itemSelecionado is None or self.itemSelecionado == '':
                return messagebox.showerror("Erro", "Selecione um item")

            if entryProduto.get() == "" or entryQtd.get() == "" or entryValor.get() == "" or comboCategoria.get() == "":
                return messagebox.showerror("Erro", "Todos os Campos devem ser preenchidos!")

            try:
                quantidade = int(entryQtd.get())
                valor = float(entryValor.get().replace(",", "."))

                item_id = self.itemSelecionado
                valores = tree.item(item_id, 'values')
                print(valores)
                produto = Produtos(
                    nome=entryProduto.get().capitalize(),
                    quantidade=quantidade,
                    valor=valor,
                    categoria=comboCategoria.get(),
                    codigo=valores[1],
                    data=valores[6]
                )
                db.update(valores[0], produto)
                preencherList()
                limparEntry()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

            except ValueError:
                messagebox.showerror("Erro", "Quantidade e valor devem ser números.")
            except Exception as e:
                messagebox.showerror("Erro inesperado", f"Ocorreu um erro:\n{e}")

        buttonAtualizar = Button(frameCadastro, text="Atualizar item", width=40, command=atualizarItem)
        buttonAtualizar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        def deleterItem():
            if self.itemSelecionado is None or self.itemSelecionado == '':
                return messagebox.showerror("Erro", "Selecione um item")

            if entryProduto.get() == "" or entryQtd.get() == "" or entryValor.get() == "":
                return messagebox.showerror("Erro", "Todos os Campos devem ser preenchidos!")

            try:
                item_id = self.itemSelecionado
                valores = tree.item(item_id, 'values')  # Essa é a tupla correta

                resposta = messagebox.askokcancel("Alerta!!!", f"remover realmente deletar esse item? '{valores[2]}'")
                if resposta:
                    db.remove(valores[0])
                    preencherList()
                    limparEntry()
                    messagebox.showinfo("Sucesso", "item removido com sucesso!!!")

            except ValueError:
                messagebox.showerror("Erro", "Quantidade e valor devem ser números.")
            except Exception as e:
                messagebox.showerror("Erro inesperado", f"Ocorreu um erro:\n{e}")

        buttonAtualizar = Button(frameCadastro, text="Deletar item", width=40, command=deleterItem)
        buttonAtualizar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.saparete = Frame(framePrincipal, bg='black', width=5)
        self.saparete.pack(side=LEFT, fill=Y)

        frameTopo = Frame(framePrincipal, bg=self.azulMedio)
        frameTopo.pack(fill=BOTH, expand=True, side=TOP)

        labelTitulo = Label(frameTopo, text="Pesquisa de produtos", font=("Arial", 16), bg=self.azulMedio, fg='white')
        labelTitulo.pack(fill=X, side=TOP)

        framePesquisa = Frame(frameTopo, bg=self.azulMedio)
        framePesquisa.pack(fill=BOTH, expand=True, side=TOP)

        labelPesquisa = Label(framePesquisa, text="Nome", font=("Arial", 12), bg=self.azulMedio, fg='white')
        labelPesquisa.pack(fill=X, side=LEFT, padx=5)

        entryPesquisa = Entry(framePesquisa, width=30)
        entryPesquisa.pack(fill=X, side=LEFT, padx=5)

        frameFiltro = Frame(frameTopo, bg=self.azulMedio)
        frameFiltro.pack(fill=BOTH, expand=True, side=BOTTOM)

        labelPesquisa = Label(frameFiltro, text="Filtrar por: ", font=("Arial", 12), bg=self.azulMedio, fg='white')
        labelPesquisa.pack(fill=X, side=LEFT, padx=5)

        self.sapareteX = Frame(framePrincipal, bg='black', width=5)
        self.sapareteX.pack(side=TOP, fill=X)

        def pesquisarItem():
            termo = entryPesquisa.get().lower()

            tree.delete(*tree.get_children())

            for produto in self.produtos:
                if termo in produto[2].lower():  # índice 2 = nome
                    tree.insert("", END, values=produto)

        entryPesquisa.bind("<KeyRelease>", lambda event: pesquisarItem())

        comboFiltro = ttk.Combobox(frameFiltro, width=12, state="readonly")
        comboFiltro["values"] = ("All", "Nome", "Quantidade", "Preço")
        comboFiltro.current(0)

        comboFiltro.pack(fill=X, side=LEFT, padx=5)

        def filtrarItens(event):
            valor = comboFiltro.get()
            if self.produtos == '':
                pass

            for item in tree.get_children():
                tree.delete(item)
            print(self.produtos)
            if valor == "All":
                for item in self.produtos:
                    tree.insert("", END, values=item)
            elif valor == "Nome":
                produtosOrdenados = sorted(self.produtos, key=lambda p: p[2].lower())
                for item in produtosOrdenados:
                    tree.insert("", END, values=item)
            elif valor == "Quantidade":
                produtosOrdenados = sorted(self.produtos, key=lambda q: q[3])
                for item in produtosOrdenados:
                    tree.insert("", END, values=item)
            elif valor == "Preço":
                produtosOrdenados = sorted(self.produtos, key=lambda q: q[4])
                for item in produtosOrdenados:
                    tree.insert("", END, values=item)

        comboFiltro.bind("<<ComboboxSelected>>", filtrarItens)

        frameCentral = Frame(framePrincipal, bg=self.azulMedio)
        frameCentral.pack(fill=BOTH, expand=True)

        colunas = ("Id", "Codigo", "Produto", "Qtd", "Preço", "Categoria", "Data")
        tree = ttk.Treeview(frameCentral, columns=colunas, show="headings", height=10)
        tree.pack(padx=10, pady=10, fill=BOTH, expand=True, side=BOTTOM)

        # Cabeçalhos
        tree.heading("Id", text="Id")
        tree.heading("Codigo", text="Codigo")
        tree.heading("Produto", text="Produto")
        tree.heading("Qtd", text="Qtd")
        tree.heading("Preço", text="Preço")
        tree.heading("Categoria", text="Categoria")
        tree.heading("Data", text="Data")

        # Tamanhos das colunas
        tree.column("Id", width=150)
        tree.column("Codigo", width=150)
        tree.column("Produto", width=150)
        tree.column("Qtd", width=10)
        tree.column("Preço", width=80)
        tree.column("Categoria", width=80)
        tree.column("Data", width=100)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        bg=self.brancoClaro,
                        fg='black',
                        rowheight=25,
                        fieldbackground=self.brancoClaro)
        style.map("Treeview", bg=[("selected", self.amareloMostarda)])

        def selecionarIten(event):
            self.itemSelecionado = tree.focus()
            if not self.itemSelecionado:
                return

            value = tree.item(self.itemSelecionado, 'values')
            if not value or len(value) < 5:
                return

            print(value)

            limparEntry()

            entryProduto.insert(0, value[2])  # Nome
            entryQtd.insert(0, value[3])  # Quantidade
            entryValor.insert(0, value[4])  # Valor
            comboCategoria.set(value[5])

        tree.bind("<<TreeviewSelect>>", selecionarIten)

        def preencherList():
            for item in tree.get_children():
                tree.delete(item)

            self.produtos = db.fetch()

            for item in self.produtos:
                tree.insert("", END, values=item)

        preencherList()
        janela.mainloop()


if __name__ == "__main__":
    Estoque()
