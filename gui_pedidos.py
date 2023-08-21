import tkinter as tk
from tkinter import messagebox
import pedidos, PedidosConnect

class PedidoGUI:
    def __init__(self, root):
        self.root = root
        self.pedidos_dao = PedidosConnect.PedidosDAO()

        self.create_widgets()
        self.root.title("Listagem de Pedidos")

    def create_widgets(self):
        # Criação dos widgets da interface

        # Label e Entry para o ID do Pedido
        self.lbl_id_pedido = tk.Label(self.root, text="ID Pedido:")
        self.lbl_id_pedido.grid(row=0, column=0, sticky="e")

        self.entry_id_pedido = tk.Entry(self.root)
        self.entry_id_pedido.grid(row=0, column=1)

        # Label e Entry para a Data do Pedido
        self.lbl_data_pedido = tk.Label(self.root, text="Data Pedido:")
        self.lbl_data_pedido.grid(row=1, column=0, sticky="e")

        self.entry_data_pedido = tk.Entry(self.root)
        self.entry_data_pedido.grid(row=1, column=1)

        # Label e Entry para o ID do Cliente
        self.lbl_id_cliente = tk.Label(self.root, text="ID Cliente:")
        self.lbl_id_cliente.grid(row=2, column=0, sticky="e")

        self.entry_id_cliente = tk.Entry(self.root)
        self.entry_id_cliente.grid(row=2, column=1)

        # Label e Entry para o Status
        self.lbl_status = tk.Label(self.root, text="Status:")
        self.lbl_status.grid(row=3, column=0, sticky="e")

        self.entry_status = tk.Entry(self.root)
        self.entry_status.grid(row=3, column=1)

        # Botões para as operações CRUD
        self.btn_criar = tk.Button(self.root, text="Criar", command=self.criar_pedido)
        self.btn_criar.grid(row=4, column=0, padx=10, pady=5)

        self.btn_ler = tk.Button(self.root, text="Ler", command=self.ler_pedido)
        self.btn_ler.grid(row=4, column=1, padx=10, pady=5)

        self.btn_atualizar = tk.Button(self.root, text="Atualizar", command=self.atualizar_pedido)
        self.btn_atualizar.grid(row=4, column=2, padx=10, pady=5)

        self.btn_deletar = tk.Button(self.root, text="Deletar", command=self.deletar_pedido)
        self.btn_deletar.grid(row=4, column=3, padx=10, pady=5)

    def criar_pedido(self):
        id_pedido = self.entry_id_pedido.get()
        data_pedido = self.entry_data_pedido.get()
        id_cliente = int(self.entry_id_cliente.get())
        status = self.entry_status.get()

        self.pedidos_dao.set_pedido(pedidos.Pedido(id_pedido, data_pedido, id_cliente, status)).Criar_pedido()

        messagebox.showinfo("Pedido Criado", "Pedido criado com sucesso!")

    def ler_pedido(self):
        id_pedido = self.entry_id_pedido.get()

        pedido = self.pedidos_dao.ler_pedido(id_pedido)

        if pedido is not None:
            self.entry_data_pedido.delete(0, tk.END)
            self.entry_data_pedido.insert(0, pedido.get_data_pedido())

            self.entry_id_cliente.delete(0, tk.END)
            self.entry_id_cliente.insert(0, pedido.get_id_cliente())

            self.entry_status.delete(0, tk.END)
            self.entry_status.insert(0, pedido.get_status())
        else:
            messagebox.showinfo("Pedido não encontrado", "Pedido não encontrado!")

    def atualizar_pedido(self):
        id_pedido = self.entry_id_pedido.get()
        data_pedido = self.entry_data_pedido.get()
        id_cliente = int(self.entry_id_cliente.get())
        status = self.entry_status.get()

        pedido = pedidos(id_pedido, data_pedido, id_cliente, status)
        self.pedidos_dao.atualizar_pedido(pedido)

        messagebox.showinfo("Pedido Atualizado", "Pedido atualizado com sucesso!")

    def deletar_pedido(self):
        id_pedido = self.entry_id_pedido.get()

        result = messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar o pedido?")

        if result:
            self.pedidos_dao.deletar_pedido(id_pedido)
            messagebox.showinfo("Pedido Deletado", "Pedido deletado com sucesso!")
            self.clear_entries()

    def clear_entries(self):
        self.entry_id_pedido.delete(0, tk.END)
        self.entry_data_pedido.delete(0, tk.END)
        self.entry_id_cliente.delete(0, tk.END)
        self.entry_status.delete(0, tk.END)

root = tk.Tk()
app = PedidoGUI(root)
root.mainloop()
