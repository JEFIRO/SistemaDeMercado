from tkinter import *
from tkinter import ttk, messagebox
from CRUD import Database
from Vendas import Vendas
from datetime import datetime


class Main:
    def __init__(self):
        self.total = 0
        self.totalComDesconto = 0

        self.azulMarinho = "#001F3F"
        self.azulMedio = "#4682B4"
        self.amareloMostarda = "#FFDB58"
        self.brancoClaro = "#F5FFFA"
        self.textoClaro = "#FAFAFA"

        db = Database("banco.db")
        dbVendas = Vendas("vendas.db")

        self.listaDeCompras = []
        self.janela = Tk()
        self.janela.title("Tela Maximizando")
        self.janela.state('zoomed')
        self.janela.resizable(False, False)

        def puxarTelaDeEstoque():
            from estoque import Estoque
            self.janela.destroy()
            Estoque()

        from tkinter import Toplevel, Button, ttk, Menu
        from datetime import datetime

        # Supondo que você já tenha a classe Vendas definida com os métodos de relatório

        def relatorio_por_dia(dbVendas):
            janela = Toplevel()
            janela.title("Relatório por Dia")
            janela.geometry("500x300")

            tree = ttk.Treeview(janela, columns=("Data", "Total"), show="headings")
            tree.heading("Data", text="Data")
            tree.heading("Total", text="Total (R$)")
            tree.column("Data", width=200)
            tree.column("Total", width=100, anchor="center")
            tree.pack(pady=20, expand=True, fill="both")

            def carregar_dados():
                for row in tree.get_children():
                    tree.delete(row)
                for data, total in dbVendas.relatorioPorDia():
                    tree.insert("", "end", values=(data, f"{total:.2f}"))

            btn = Button(janela, text="Carregar Relatório", command=carregar_dados)
            btn.pack(pady=10)

        def relatorio_por_produto(dbVendas):
            janela = Toplevel()
            janela.title("Relatório por Produto")
            janela.geometry("600x300")

            tree = ttk.Treeview(janela, columns=("Produto", "Quantidade", "Total"), show="headings")
            tree.heading("Produto", text="Produto")
            tree.heading("Quantidade", text="Quantidade")
            tree.heading("Total", text="Total (R$)")
            tree.column("Produto", width=250)
            tree.column("Quantidade", width=100, anchor="center")
            tree.column("Total", width=100, anchor="center")
            tree.pack(pady=20, expand=True, fill="both")

            def carregar_dados():
                for row in tree.get_children():
                    tree.delete(row)
                for produto, qtd, total in dbVendas.relatorioPorProduto():
                    tree.insert("", "end", values=(produto, qtd, f"{total:.2f}"))

            btn = Button(janela, text="Carregar Relatório", command=carregar_dados)
            btn.pack(pady=10)

        def relatorio_por_categoria(dbVendas):
            janela = Toplevel()
            janela.title("Relatório por Categoria")
            janela.geometry("600x300")

            tree = ttk.Treeview(janela, columns=("Categoria", "Quantidade", "Total"), show="headings")
            tree.heading("Categoria", text="Categoria")
            tree.heading("Quantidade", text="Quantidade")
            tree.heading("Total", text="Total (R$)")
            tree.column("Categoria", width=250)
            tree.column("Quantidade", width=100, anchor="center")
            tree.column("Total", width=100, anchor="center")
            tree.pack(pady=20, expand=True, fill="both")

            def carregar_dados():
                for row in tree.get_children():
                    tree.delete(row)
                for categoria, qtd, total in dbVendas.relatorioPorCategoria():
                    tree.insert("", "end", values=(categoria, qtd, f"{total:.2f}"))

            btn = Button(janela, text="Carregar Relatório", command=carregar_dados)
            btn.pack(pady=10)

        def relatorio_por_forma_pagamento(dbVendas):
            janela = Toplevel()
            janela.title("Relatório por Forma de Pagamento")
            janela.geometry("500x300")

            tree = ttk.Treeview(janela, columns=("Forma de Pagamento", "Total"), show="headings")
            tree.heading("Forma de Pagamento", text="Forma de Pagamento")
            tree.heading("Total", text="Total (R$)")
            tree.column("Forma de Pagamento", width=250)
            tree.column("Total", width=100, anchor="center")
            tree.pack(pady=20, expand=True, fill="both")

            def carregar_dados():
                for row in tree.get_children():
                    tree.delete(row)
                for forma, total in dbVendas.relatorioPorFormaDePagamento():
                    tree.insert("", "end", values=(forma, f"{total:.2f}"))

            btn = Button(janela, text="Carregar Relatório", command=carregar_dados)
            btn.pack(pady=10)

        def relatorio_detalhado(dbVendas):
            janela = Toplevel()
            janela.title("Relatório Detalhado")
            janela.geometry("800x400")

            tree = ttk.Treeview(janela,
                                columns=("Data", "Produto", "Quantidade", "Preço", "Categoria", "Forma de Pagamento"),
                                show="headings")
            tree.heading("Data", text="Data")
            tree.heading("Produto", text="Produto")
            tree.heading("Quantidade", text="Quantidade")
            tree.heading("Preço", text="Preço (R$)")
            tree.heading("Categoria", text="Categoria")
            tree.heading("Forma de Pagamento", text="Forma de Pagamento")

            tree.column("Data", width=100)
            tree.column("Produto", width=200)
            tree.column("Quantidade", width=80, anchor="center")
            tree.column("Preço", width=80, anchor="center")
            tree.column("Categoria", width=150)
            tree.column("Forma de Pagamento", width=150)

            tree.pack(pady=20, expand=True, fill="both")

            def carregar_dados():
                for row in tree.get_children():
                    tree.delete(row)
                for data, produto, quantidade, preco, categoria, forma in dbVendas.relatorioDetalhado():
                    tree.insert("", "end", values=(data, produto, quantidade, f"{preco:.2f}", categoria, forma))

            btn = Button(janela, text="Carregar Relatório", command=carregar_dados)
            btn.pack(pady=10)

        menuBarra = Menu(self.janela)

        # Menu "Menu"
        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Estoque", command=puxarTelaDeEstoque)
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=self.janela.quit)
        menuBarra.add_cascade(label="Menu", menu=menuArquivo)

        # Menu "Relatórios"
        menuRelatorios = Menu(menuBarra, tearoff=0)
        menuRelatorios.add_command(label="Por Dia", command=lambda: relatorio_por_dia(dbVendas))
        menuRelatorios.add_command(label="Por Produto", command=lambda: relatorio_por_produto(dbVendas))
        menuRelatorios.add_command(label="Por Categoria", command=lambda: relatorio_por_categoria(dbVendas))
        menuRelatorios.add_command(label="Por Forma de Pagamento",
                                   command=lambda: relatorio_por_forma_pagamento(dbVendas))
        menuRelatorios.add_command(label="Relatório Detalhado", command=lambda: relatorio_detalhado(dbVendas))
        menuBarra.add_cascade(label="Relatórios", menu=menuRelatorios)

        # Definir a barra de menus da janela
        self.janela.config(menu=menuBarra)

        self.framePrincipal = Frame(self.janela, bg=self.azulMarinho)
        self.framePrincipal.pack(expand=True, fill=BOTH)

        # Lateral fixo
        self.frameLateral = Frame(self.framePrincipal, bg=self.azulMedio, width=400)
        self.frameLateral.pack(side=LEFT, fill=Y)

        labelTitulo = Label(self.frameLateral, text="Valor Da Compra", font=("Arial", 18), bg=self.azulMarinho,
                            fg=self.brancoClaro)
        labelTitulo.pack(fill=X, pady=10, padx=5)

        self.valorDaCompra = StringVar()
        self.valorDaCompra.set("00,00")
        labelValor = Label(self.frameLateral, textvariable=self.valorDaCompra, font=("Arial", 18), bg=self.azulMarinho,
                           fg=self.brancoClaro)
        labelValor.pack(fill=X, pady=10, padx=5)

        labelDescontoTitulo = Label(self.frameLateral, text="Desconto", font=("Arial", 18), bg=self.azulMarinho,
                                    fg=self.brancoClaro)
        labelDescontoTitulo.pack(fill=X, pady=10, padx=5)

        self.desconto = StringVar()
        self.desconto.set('0')
        labelDescontoValor = Label(self.frameLateral, textvariable=self.desconto, font=("Arial", 18),
                                   bg=self.azulMarinho, fg=self.brancoClaro)
        labelDescontoValor.pack(fill=X, pady=10, padx=5)

        labelTotalTitulo = Label(self.frameLateral, text="Valor Total", font=("Arial", 18), bg=self.azulMarinho,
                                 fg=self.brancoClaro)
        labelTotalTitulo.pack(fill=X, pady=10, padx=5)

        self.valorTotal = StringVar()
        self.valorTotal.set("00,00")
        labelTotalValor = Label(self.frameLateral, textvariable=self.valorTotal, font=("Arial", 18),
                                bg=self.azulMarinho, fg=self.brancoClaro)
        labelTotalValor.pack(fill=X, pady=10, padx=5)

        self.saparete = Frame(self.framePrincipal, bg=self.brancoClaro, width=2)
        self.saparete.pack(side=LEFT, fill=Y)

        # Frame à direita que ocupa o resto do espaço
        self.frameDireita = Frame(self.framePrincipal)
        self.frameDireita.pack(side=LEFT, fill=BOTH, expand=True)

        self.frameCentral = Frame(self.frameDireita, bg=self.azulMedio, height=400)
        self.frameCentral.pack(side=TOP, fill=BOTH, expand=True)

        colunas = ("Id", "Codigo", "Produto", "Qtd", "Preço")
        self.tree = ttk.Treeview(self.frameCentral, columns=colunas, show="headings", height=10)
        self.tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Cabeçalhos
        self.tree.heading("Id", text="Id")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Qtd", text="Qtd")
        self.tree.heading("Preço", text="Preço")

        # Tamanhos das colunas
        self.tree.column("Id", width=10)
        self.tree.column("Codigo", width=150)
        self.tree.column("Produto", width=150)
        self.tree.column("Qtd", width=10)
        self.tree.column("Preço", width=80)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        bg=self.brancoClaro,
                        fg='black',
                        rowheight=25,
                        fieldbackground=self.brancoClaro)
        style.map("Treeview", bg=[("selected", self.amareloMostarda)])

        self.frameInferior = Frame(self.frameDireita, bg=self.azulMarinho, height=200)
        self.frameInferior.pack(side=BOTTOM, fill=X)

        labelCodigo = Label(self.frameInferior, text="Código", bg=self.azulMarinho,
                            fg=self.textoClaro, font=("Arial", 14))
        labelCodigo.grid(row=0, column=0, pady=10, padx=5)

        entryCodigo = Entry(self.frameInferior, width=15)
        entryCodigo.grid(row=0, column=1, pady=10, padx=5)

        def calcularValorDaCompra():
            self.total = 0
            for item in self.listaDeCompras:
                try:
                    qtd = int(item[3])
                    preco = float(item[4])
                    if qtd >= 1:
                        self.total += qtd * preco
                except (ValueError, TypeError):
                    pass

            self.valorDaCompra.set(f"{self.total:.2f}")
            calcularTotal()  # chama aqui, depois do total calculado

        def calcularTotal():
            if self.total >= 40 and self.total <= 199:
                desconto = self.total - (self.total * 0.05)
                self.totalComDesconto = desconto
                self.desconto.set("5%")
                self.valorTotal.set(f"{desconto:.2f}")
            elif self.total >= 200:
                desconto = self.total - (self.total * 0.1)
                self.totalComDesconto = desconto
                self.desconto.set("10%")
                self.valorTotal.set(f"{desconto:.2f}")
            else:
                self.desconto.set("0%")
                self.valorTotal.set(f"{self.total:.2f}")

        def pesquisarItem(event):
            try:
                termo = int(entryCodigo.get())
                self.tupla = db.findById(termo)

                if self.tupla:
                    self.itemTemp = list(self.tupla)
                    entryQtd.delete(0, END)
                    entryQtd.focus_set()
                else:
                    messagebox.showinfo("Aviso", "Produto não encontrado")
            except ValueError:
                messagebox.showerror("Erro", "Digite um código numérico válido")

        def confirmarQtd(event):
            try:
                qtd = entryQtd.get()

                # Se vazio ou inválido, define como 1
                if qtd == '' or not qtd.isdigit() or int(qtd) <= 0:
                    qtd = 1
                else:
                    qtd = int(qtd)

                # Verifica se há estoque suficiente
                estoque = self.tupla[3]
                if qtd > estoque:
                    messagebox.showerror("Erro", "Não há itens suficientes no estoque")
                    return

                self.itemTemp[3] = qtd
                self.listaDeCompras.append(self.itemTemp)
                self.tree.insert("", END, values=self.itemTemp)

                calcularValorDaCompra()

                entryCodigo.delete(0, END)
                entryQtd.delete(0, END)
                entryCodigo.focus_set()

            except Exception as e:
                print("Erro:", e)
                messagebox.showerror("Erro", "Digite uma quantidade válida")

        labelQtd = Label(self.frameInferior, text="Qtd", bg=self.azulMarinho,
                         fg=self.textoClaro, font=("Arial", 14))
        labelQtd.grid(row=0, column=2, pady=10, padx=5)

        entryQtd = Entry(self.frameInferior, width=15)
        entryQtd.grid(row=0, column=3, pady=10, padx=5)

        entryCodigo.bind("<Return>", pesquisarItem)
        entryQtd.bind("<Return>", confirmarQtd)

        def cancelarVenda(event):
            if self.listaDeCompras:
                msg = messagebox.askokcancel("Alerta", "Deseja realmente cancelar esse compra?")
                if msg:
                    limparTudo()

        def limparTudo():
            for item in self.tree.get_children():
                self.tree.delete(item)

            self.total = 0
            self.totalComDesconto = 0
            self.listaDeCompras = []

            self.valorTotal.set("00,00")
            self.desconto.set('0')
            self.valorDaCompra.set("00,00")

        def finalizarVenda(event):
            janela = Toplevel()
            janela.title("Finalizar Venda")
            janela.geometry("500x500")
            janela.resizable(False, False)
            janela.configure(bg=self.azulMarinho)
            janela.focus_set()
            Label(janela, text="Finalizar Venda", font=("Arial", 20, "bold"), bg="#001F3F", fg="white").pack(pady=20)

            Label(janela, text="Valor Total:", font=("Arial", 14), bg="#001F3F", fg="white").pack(pady=5)

            def get_valor_final():
                return self.totalComDesconto if self.totalComDesconto else self.total

            valor = StringVar()
            valor.set(f"{get_valor_final():.2f}")
            Label(janela, textvariable=valor, font=("Arial", 14), bg="#001F3F", fg="white").pack(pady=5)

            valorASerPago = StringVar()
            valorASerPago.set(f"Valor a ser pago: R$ {get_valor_final():.2f}")
            valorAserPago = Label(janela, textvariable=valorASerPago, fg=self.brancoClaro, bg=self.azulMarinho,
                                  font=("Arial", 16), pady=10)

            pagamento = ttk.Combobox(janela, width=17, state="readonly")
            pagamento["values"] = ("Pix", "Dinheiro", "Credito 1X", "Debito")
            pagamento.pack()

            def calcularTroco():
                try:
                    total = float(self.totalComDesconto)
                    pago = float(entryPago.get().replace(",", "."))
                    troco = pago - total
                    labelTroco.config(text=f"Troco: R$ {troco:.2f}")
                except ValueError:
                    labelTroco.config(text="Entrada inválida")

            def atualizarEstoque():
                try:
                    for item in self.listaDeCompras:
                        db.updateQTD(int(item[0]), int(item[3]))
                except:
                    pass
                finally:
                    limparTudo()
                    janela.destroy()

            def confirmarVenda(event):
                atualizarEstoque()
                for item in self.listaDeCompras:
                    dbVendas.registrarVenda(item[2], int(item[3]), float(item[4]), item[5], item[6],
                                            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                            )

            labelPago = Label(janela, text="Valor Pago:", font=("Arial", 14), bg="#001F3F", fg="white")
            entryPago = Entry(janela, font=("Arial", 14))
            troco = Button(janela, text="Calcular Troco", font=("Arial", 12))
            labelTroco = Label(janela, text="Troco: R$ 0.00", font=("Arial", 14), bg="#001F3F", fg="white")
            confirmar = Button(janela, text="Confirmar Venda", font=("Arial", 14), bg="#FFDB58", command=confirmarVenda)

            def on_key_press(event):
                if event.char in ['1', '2', '3', '4']:
                    indice = int(event.char) - 1
                    if indice < len(pagamento["values"]):
                        pagamento.current(indice)

                        if pagamento.get() == "Dinheiro":
                            valorAserPago.pack_forget()
                            labelPago.pack(pady=5)
                            entryPago.pack(pady=5)
                            troco.pack(pady=10)
                            labelTroco.pack(pady=20)
                            confirmar.pack_forget()
                            confirmar.pack(pady=20)
                        else:
                            labelPago.pack_forget()
                            entryPago.pack_forget()
                            labelTroco.pack_forget()
                            troco.pack_forget()
                            valorAserPago.pack_forget()
                            valorAserPago.pack()
                            confirmar.pack_forget()
                            confirmar.pack(pady=20)

            janela.bind("<KeyPress>", on_key_press)
            janela.bind("<Return>", confirmarVenda)

            # Troco

        self.janela.bind("<F5>", finalizarVenda)
        self.janela.bind("<F6>", cancelarVenda)
        self.janela.mainloop()


if __name__ == "__main__":
    Main()
