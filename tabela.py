import tkinter as tk
from tkinter import ttk
import pedidos, PedidosConnect

class TabelaPedidosClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Pedidos e Clientes")

        # Criação do Treeview
        self.treeview = ttk.Treeview(self.root)
        self.treeview["columns"] = ("ID", "Nome", "Telefone", "Endereço", "ID Pedido", "Data Pedido", "Status")
        self.treeview.heading("#0", text="")
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.heading("ID", text="ID")
        self.treeview.column("ID", width=50, anchor=tk.CENTER)
        self.treeview.heading("Nome", text="Nome")
        self.treeview.column("Nome", width=150, anchor=tk.W)
        self.treeview.heading("Telefone", text="Telefone")
        self.treeview.column("Telefone", width=100, anchor=tk.CENTER)
        self.treeview.heading("Endereço", text="Endereço")
        self.treeview.column("Endereço", width=200, anchor=tk.W)
        self.treeview.heading("ID Pedido", text="ID Pedido")
        self.treeview.column("ID Pedido", width=80, anchor=tk.CENTER)
        self.treeview.heading("Data Pedido", text="Data Pedido")
        self.treeview.column("Data Pedido", width=100, anchor=tk.CENTER)
        self.treeview.heading("Status", text="Status")
        self.treeview.column("Status", width=100, anchor=tk.CENTER)

        # Inserir dados de exemplo na tabela
        self.inserir_dados_exemplo()

        # Barra de rolagem vertical
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Filtro
        self.filtro_var = tk.StringVar()
        self.filtro_entry = tk.Entry(self.root, textvariable=self.filtro_var)
        self.filtro_entry.pack()
        self.filtro_entry.bind('<KeyRelease>', self.filtrar_tabela)

        # Posicionamento do Treeview
        self.treeview.pack()

    def inserir_dados_exemplo(self):
        # Inserir dados de exemplo na tabela (clientes e pedidos)
        self.conexao = PedidosConnect.PedidosDAO()
        items=self.conexao.Read_pedido()
        for i in items:
            self.treeview.insert("", "end", text="", values=(i[3], i[4], i[6], i[5],
                                                             i[0], i[1], i[2]))

    def filtrar_tabela(self, event=None):
        filtro = self.filtro_var.get().lower()
        # Percorre todas as linhas da tabela
        for row_id in self.treeview.get_children():
            # Obtém os valores da linha
            values = self.treeview.item(row_id)["values"]
            # Verifica se algum valor da linha corresponde ao filtro
            if any(filtro in str(value).lower() for value in values):
                self.treeview.item(row_id, tags=())
            else:
                self.treeview.item(row_id, tags=("hidden",))

root = tk.Tk()
app = TabelaPedidosClientes(root)
root.mainloop()
