from tkinter import *
from tkinter import messagebox

from CRUD import Database
from Vendas import Vendas


class Main:
    def __init__(self):
        self.itemTemp = None
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
        self.janela.title("Vendas")
        self.janela.state('zoomed')
        self.janela.resizable(False, False)

        def puxarTelaDeEstoque():
            from estoque import Estoque
            self.janela.destroy()
            Estoque()

        from tkinter import Toplevel, Button, ttk, Menu
        from datetime import datetime

        menuBarra = Menu(self.janela)

        # Menu "Menu"
        menuArquivo = Menu(menuBarra, tearoff=0)
        menuArquivo.add_command(label="Estoque", command=puxarTelaDeEstoque)
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Sair", command=self.janela.quit)
        menuBarra.add_cascade(label="Menu", menu=menuArquivo)

        menuBarra.add_cascade(label="Relatórios")

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

        self.frameDireita = Frame(self.framePrincipal)
        self.frameDireita.pack(side=LEFT, fill=BOTH, expand=True)

        self.frameCentral = Frame(self.frameDireita, bg=self.azulMedio, height=400)
        self.frameCentral.pack(side=TOP, fill=BOTH, expand=True)

        colunas = ("Id", "Codigo", "Produto", "Qtd", "Preço")
        self.tree = ttk.Treeview(self.frameCentral, columns=colunas, show="headings", height=10)
        self.tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.tree.heading("Id", text="Id")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Qtd", text="Qtd")
        self.tree.heading("Preço", text="Preço")

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

        entryCodigo = Entry(
            self.frameInferior,
            width=15,
            font=("Arial", 12),
            bg=self.brancoClaro,
            fg=self.azulMarinho,
            insertbackground=self.azulMarinho,
            highlightbackground=self.azulMedio,
            highlightcolor=self.azulMedio,
            highlightthickness=1,
            relief="solid",
            bd=1
        )
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
            calcularTotal()

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

                print(self.tupla)

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

                if qtd == '' or not qtd.isdigit() or int(qtd) <= 0:
                    qtd = 1
                else:
                    qtd = int(qtd)

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

        entryQtd = Entry(
            self.frameInferior,
            width=15,
            font=("Arial", 12),
            bg=self.brancoClaro,  # fundo claro
            fg=self.azulMarinho,  # texto escuro para contraste
            insertbackground=self.azulMarinho,  # cor do cursor
            highlightbackground=self.azulMedio,  # borda externa
            highlightcolor=self.azulMedio,
            highlightthickness=1,
            relief="solid",
            bd=1
        )
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
                try:
                    return float(self.totalComDesconto) if self.totalComDesconto else float(self.total)
                except:
                    return 0.0

            valor = StringVar(value=f"{get_valor_final():.2f}")
            Label(janela, textvariable=valor, font=("Arial", 14), bg="#001F3F", fg="white").pack(pady=5)

            valorASerPago = StringVar(value=f"Valor a ser pago: R$ {get_valor_final():.2f}")
            valorAserPago = Label(janela, textvariable=valorASerPago, fg=self.brancoClaro, bg=self.azulMarinho,
                                  font=("Arial", 16), pady=10)

            # Estilo do Combobox
            style = ttk.Style()
            style.theme_use("default")
            style.configure("TCombobox", fieldbackground=self.azulMarinho, background="white", foreground="black")

            pagamento = ttk.Combobox(janela, width=17, state="readonly")
            pagamento["values"] = ("Pix", "Dinheiro", "Credito 1X", "Debito")
            pagamento.pack()

            def calcularTroco():
                try:
                    total = get_valor_final()
                    pago = float(entryPago.get().replace(",", "."))
                    troco_valor = pago - total
                    labelTroco.config(text=f"Troco: R$ {troco_valor:.2f}")
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

            def confirmarVenda(event=None):
                if pagamento.get() not in pagamento["values"]:
                    messagebox.showwarning("Forma de pagamento inválida", "Selecione uma forma de pagamento válida.")
                    return
                for item in self.listaDeCompras:
                    dbVendas.registrarVenda(
                        item[2],
                        int(item[3]),
                        pagamento.get(),
                        item[5],
                        item[6],
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                atualizarEstoque()

            labelPago = Label(janela, text="Valor Pago:", font=("Arial", 14), bg="#001F3F", fg="white")
            entryPago = Entry(janela, font=("Arial", 14))
            troco = Button(janela, text="Calcular Troco", font=("Arial", 12), command=calcularTroco)
            labelTroco = Label(janela, text="Troco: R$ 0.00", font=("Arial", 14), bg="#001F3F", fg="white")
            confirmar = Button(janela, text="Confirmar Venda", font=("Arial", 14), bg="#FFDB58", command=confirmarVenda)

            def bloquear_digitos_invalidos(event):
                if event.char.isdigit() or event.char == ',':
                    return
                elif event.keysym == "BackSpace":
                    return
                else:
                    return "break"

            entryPago.bind("<Key>", bloquear_digitos_invalidos)

            def on_key_press(event):
                widget_focado = janela.focus_get()

                if widget_focado == entryPago:
                    return

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

        def atualizarTreeView():
            for item in self.tree.get_children():
                self.tree.delete(item)
            for itemAdd in self.listaDeCompras:
                self.tree.insert("", END, values=itemAdd)

        def atualizarVenda(event):
            selecionado = self.tree.focus()
            if not selecionado:
                return

            item = self.tree.item(selecionado, 'values')
            if not item:
                return

            produto = None

            for items in self.listaDeCompras:
                if str(items[0]) == str(item[0]):
                    produto = items
                    break

            if not produto:
                print("Produto não encontrado na lista.")
                return

            janela = Toplevel(self.janela)
            janela.geometry("300x200")
            janela.title("Editar Item")
            janela.resizable(False, False)

            framePrincipal = Frame(janela, bg=self.azulMarinho)
            framePrincipal.pack(fill=BOTH, expand=True)

            Label(framePrincipal, text="Quantidade:", font=("Arial", 16, "bold"), bg=self.azulMarinho,
                  fg=self.brancoClaro).pack(pady=10)
            entrada_qtd = Entry(framePrincipal, font=("Arial", 12))
            entrada_qtd.insert(0, str(produto[3]))
            entrada_qtd.pack()
            entrada_qtd.focus_set()
            janela.bind("<Escape>", lambda event: janela.destroy())

            def salvarEvent(event):
                salvar()

            def salvar():
                try:
                    nova_qtd = int(entrada_qtd.get())
                    if nova_qtd <= 0:
                        raise ValueError

                    registro = db.findById(int(item[0]))
                    print(registro)
                    if nova_qtd > int(registro[3]):
                        messagebox.showerror("Erro", "não á items suficientes no estoque")
                        return
                    produto[3] = nova_qtd
                    atualizarTreeView()
                    calcularValorDaCompra()
                    entryCodigo.focus_set()
                    janela.destroy()
                except ValueError:
                    messagebox.showerror("Erro", "Insira uma quantidade válida.")

            buttonSave = Button(framePrincipal, text="Salvar", command=salvar)
            buttonSave.pack(pady=10)

            janela.transient(self.janela)
            janela.grab_set()
            janela.bind("<Return>", salvarEvent)

            self.janela.wait_window(janela)

        def deletarItemDaLista(event):

            selecionado = self.tree.focus()
            if not selecionado:
                return

            item = self.tree.item(selecionado, 'values')
            resposta = messagebox.askokcancel("Alerta", f"deseja realmente remover esse item? {item[2]}")

            if resposta:
                self.tree.delete(selecionado)
                if not item:
                    return

                for items in self.listaDeCompras:
                    if str(items[0]) == str(item[0]):
                        self.listaDeCompras.remove(items)
                calcularValorDaCompra()
            else:
                return

        self.janela.bind("<F5>", finalizarVenda)
        self.janela.bind("<F6>", atualizarVenda)
        self.janela.bind("<F8>", deletarItemDaLista)
        self.janela.bind("<F9>", cancelarVenda)

        self.tree.bind("<Double-1>", atualizarVenda)

        entryCodigo.focus_set()
        self.janela.mainloop()


if __name__ == "__main__":
    Main()
