""" import tkinter as tk
from tkinter import messagebox
import gui_clientes
import gui_pedidos

class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")

        # Botões para acessar as telas de Gerenciamento de Cliente e Pedidos
        self.btn_gerenciamento_cliente = tk.Button(self.root, text="Gerenciamento de Cliente", command=self.abrir_tela_cliente)
        self.btn_gerenciamento_cliente.pack()

        self.btn_gerenciamento_pedidos = tk.Button(self.root, text="Gerenciamento de Pedidos", command=self.abrir_tela_pedidos)
        self.btn_gerenciamento_pedidos.pack()

        # Variáveis de controle das telas abertas
        self.tela_cliente_aberta = False
        self.tela_pedidos_aberta = False

    def abrir_tela_cliente(self):
        if not self.tela_cliente_aberta:  # Verifica se a tela de clientes já está aberta
            root_cliente = tk.Toplevel(self.root)  # Cria uma nova janela (top-level) vinculada à janela principal
            app_cliente = gui_clientes.ClienteGUI(root_cliente)
            self.tela_cliente_aberta = True

    def abrir_tela_pedidos(self):
        if not self.tela_pedidos_aberta:  # Verifica se a tela de pedidos já está aberta
            root_pedidos = tk.Toplevel(self.root)  # Cria uma nova janela (top-level) vinculada à janela principal
            app_pedidos = gui_pedidos.PedidoGUI(root_pedidos)
            self.tela_pedidos_aberta = True


root = tk.Tk()
app = TelaPrincipal(root)
root.mainloop()
 """
 
import tkinter as tk
from tkinter import messagebox
import gui_clientes
import gui_pedidos


class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")

        # Botões para acessar as telas de Gerenciamento de Cliente e Pedidos
        self.btn_gerenciamento_cliente = tk.Button(self.root, text="Gerenciamento de Cliente", command=self.abrir_tela_cliente)
        self.btn_gerenciamento_cliente.pack()

        self.btn_gerenciamento_pedidos = tk.Button(self.root, text="Gerenciamento de Pedidos", command=self.abrir_tela_pedidos)
        self.btn_gerenciamento_pedidos.pack()

        # Botão para abrir a tabela de Pedidos e Clientes
        self.btn_tabela_pedidos_clientes = tk.Button(self.root, text="Tabela de Pedidos e Clientes", command=self.abrir_tabela_pedidos_clientes)
        self.btn_tabela_pedidos_clientes.pack()

    def abrir_tela_cliente(self):
        self.root.destroy()  # Fecha a tela atual
        root_cliente = tk.Tk()
        app_cliente = gui_clientes.ClienteGUI(root_cliente)
        root_cliente.mainloop()

    def abrir_tela_pedidos(self):
        self.root.destroy()  # Fecha a tela atual
        root_pedidos = tk.Tk()
        app_pedidos = gui_pedidos.PedidoGUI(root_pedidos)
        root_pedidos.mainloop()

    def abrir_tabela_pedidos_clientes(self):
        root_tabela = tk.Tk()
        app_tabela = TabelaPedidosClientes(root_tabela)
        root_tabela.mainloop()


import tkinter as tk
from tkinter import ttk

class TabelaPedidosClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Pedidos e Clientes")

        # Criação da tabela
        self.table = ttk.Treeview(self.root)
        self.table["columns"] = ("ID Pedido", "Data Pedido", "ID Cliente", "Status")
        self.table.heading("#0", text="ID")
        self.table.column("#0", width=50)
        self.table.heading("ID Pedido", text="ID Pedido")
        self.table.column("ID Pedido", width=100)
        self.table.heading("Data Pedido", text="Data Pedido")
        self.table.column("Data Pedido", width=150)
        self.table.heading("ID Cliente", text="ID Cliente")
        self.table.column("ID Cliente", width=100)
        self.table.heading("Status", text="Status")
        self.table.column("Status", width=100)
        self.table.pack()

        # Botão de filtro
        self.btn_filtrar = tk.Button(self.root, text="Filtrar", command=self.filtrar_pedidos_clientes)
        self.btn_filtrar.pack()

    def filtrar_pedidos_clientes(self):
        # Implemente o código para filtrar os pedidos e clientes na tabela
        pass

root = tk.Tk()
app = TabelaPedidosClientes(root)
root.mainloop()




root = tk.Tk()
app = TelaPrincipal(root)
root.mainloop()
