import tkinter as tk
from tkinter import messagebox
import clientes, ClienteConnect

class ClienteGUI:
    def __init__(self, root):
        self.root = root
        self.clientes_dao = ClienteConnect.connect()

        self.create_widgets()
        self.root.title("Gerenciamento de Clientes")

    def create_widgets(self):
        # Criação dos widgets da interface

        # Label e Entry para o ID do Cliente
        self.lbl_id_cliente = tk.Label(self.root, text="ID Cliente:")
        self.lbl_id_cliente.grid(row=0, column=0, sticky="e")

        self.entry_id_cliente = tk.Entry(self.root)
        self.entry_id_cliente.grid(row=0, column=1)

        # Label e Entry para o Nome
        self.lbl_nome = tk.Label(self.root, text="Nome:")
        self.lbl_nome.grid(row=1, column=0, sticky="e")

        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=1, column=1)

        # Label e Entry para o Telefone
        self.lbl_telefone = tk.Label(self.root, text="Telefone:")
        self.lbl_telefone.grid(row=2, column=0, sticky="e")

        self.entry_telefone = tk.Entry(self.root)
        self.entry_telefone.grid(row=2, column=1)

        # Label e Entry para o Endereço
        self.lbl_endereco = tk.Label(self.root, text="Endereço:")
        self.lbl_endereco.grid(row=3, column=0, sticky="e")

        self.entry_endereco = tk.Entry(self.root)
        self.entry_endereco.grid(row=3, column=1)

        # Botões para as operações CRUD
        self.btn_criar = tk.Button(self.root, text="Criar", command=self.criar_cliente)
        self.btn_criar.grid(row=4, column=0, padx=10, pady=5)

        self.btn_ler = tk.Button(self.root, text="Ler", command=self.ler_cliente)
        self.btn_ler.grid(row=4, column=1, padx=10, pady=5)

        self.btn_atualizar = tk.Button(self.root, text="Atualizar", command=self.atualizar_cliente)
        self.btn_atualizar.grid(row=4, column=2, padx=10, pady=5)

        self.btn_deletar = tk.Button(self.root, text="Deletar", command=self.deletar_cliente)
        self.btn_deletar.grid(row=4, column=3, padx=10, pady=5)

    def criar_cliente(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()

        cliente = clientes.cliente(nome=nome, telefone=telefone, endereço=endereco)
        self.clientes_dao.set_clientes(cliente).Criar_cliente()


        messagebox.showinfo("Cliente Criado", "Cliente criado com sucesso!")

    def ler_cliente(self):
        id_cliente = int(self.entry_id_cliente.get())

        cliente = self.clientes_dao.Read_cliente(id_cliente)

        if cliente is not None:
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, cliente.get_nome())

            self.entry_telefone.delete(0, tk.END)
            self.entry_telefone.insert(0, cliente.get_telefone())

            self.entry_endereco.delete(0, tk.END)
            self.entry_endereco.insert(0, cliente.get_endereco())
        else:
            messagebox.showinfo("Cliente não encontrado", "Cliente não encontrado!")

    def atualizar_cliente(self):
        id_cliente = int(self.entry_id_cliente.get())
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()

        cliente = clientes(id=id_cliente, nome=nome, telefone=telefone, endereco=endereco)
        self.clientes_dao.Update_cliente(cliente)

        messagebox.showinfo("Cliente Atualizado", "Cliente atualizado com sucesso!")

    def deletar_cliente(self):
        id_cliente = int(self.entry_id_cliente.get())

        result = messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar o cliente?")

        if result:
            self.clientes_dao.deletar_cliente(id_cliente)
            messagebox.showinfo("Cliente Deletado", "Cliente deletado com sucesso!")
            self.clear_entries()

    def clear_entries(self):
        self.entry_id_cliente.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)

root = tk.Tk()
app = ClienteGUI(root)
root.mainloop()