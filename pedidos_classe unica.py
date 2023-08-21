import tkinter as tk
import psycopg2
from tkinter import messagebox
from tkinter import ttk
from datetime import date

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

# Configuração da janela principal
root = tk.Tk()
root.title("Solicitar Pedido")
root.geometry("400x400")

# Tabela para exibir o pedido e o ID do cliente
tree = ttk.Treeview(root)
tree["columns"] = ("Pedido", "ID do Cliente")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Pedido", anchor=tk.CENTER, width=150)
tree.column("ID do Cliente", anchor=tk.CENTER, width=150)
tree.heading("Pedido", text="Pedido")
tree.heading("ID do Cliente", text="ID do Cliente")
tree.pack()

# Criar uma instância do cursor para executar as consultas SQL
cur = conn.cursor()

""" def atualizar_tabela():
    try:
        # Limpar a tabela
        tree.delete(*tree.get_children())

        # Buscar os pedidos do banco de dados
        cur.execute("SELECT Pedidos.nome, Clientes.id_cliente FROM Pedidos JOIN Clientes ON Pedidos.cliente = Clientes.id_cliente")
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

        print("Tabela atualizada com sucesso!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao atualizar a tabela:", error) """
def pesquisar_pedido():
    id_cliente = entry_pesquisa.get()
    
    if not id_cliente:
        messagebox.showwarning("Aviso", "É necessário fornecer um ID de cliente.")
        return
    
    try:
        # Limpar a tabela
        tree.delete(*tree.get_children())
        
        # Consultar os pedidos do cliente específico
        cur.execute("SELECT Pedidos.nome, Clientes.id_cliente FROM Pedidos, Clientes WHERE Pedidos.Cliente = %s", (id_cliente,))
        rows = cur.fetchall()
        
        for row in rows:
            tree.insert("", tk.END, values=row)
        
        print("Pesquisa concluída com sucesso!")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao pesquisar o pedido:", error)
def registrar_pedido():

    cliente = entry_id_cliente.get()
    nome = entry_nome_pedido.get()

    if not nome or not cliente:
        messagebox.showwarning("Aviso", "É necessário preencher todos os campos.")
        return

    try:
        # Obter a data atual
        data_pedido = date.today()

        # Definir o status inicial do pedido como "Em andamento"
        status = "Em andamento"

        # Inserir o pedido no banco de dados
        cur.execute(
            "INSERT INTO Pedidos (nome, data_pedido, cliente, status) VALUES (%s, %s, %s, %s)",
            (nome, data_pedido, cliente, status)
        )

        # Confirmar a transação
        conn.commit()

        print("Pedido registrado com sucesso!")

        # Exibir o pedido e o ID do cliente na tabela
        tree.insert("", tk.END, values=(nome, cliente))

        # Limpar os campos de entrada
        entry_nome_pedido.delete(0, tk.END)
        entry_id_cliente.delete(0, tk.END)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao registrar o pedido:", error)

def fechar_conexao():
    # Fechar o cursor e a conexão com o banco de dados
    cur.close()
    conn.close()

# Rótulos e campos de entrada

label_pesquisa = tk.Label(root, text="Pesquisar por ID do Cliente:")
label_pesquisa.pack()
label_pesquisa.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

entry_pesquisa = tk.Entry(root)
entry_pesquisa.pack()
entry_pesquisa.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

label_nome_pedido = tk.Label(root, text="Nome do Pedido:")
label_nome_pedido.pack()
label_nome_pedido.place(relx=0.30, rely=0.7, anchor=tk.CENTER)

entry_nome_pedido = tk.Entry(root)
entry_nome_pedido.pack()
entry_nome_pedido.place(relx=0.6, rely=0.7, anchor=tk.CENTER)

label_id_cliente = tk.Label(root, text="ID do Cliente:")
label_id_cliente.pack()
label_id_cliente.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

entry_id_cliente = tk.Entry(root)
entry_id_cliente.pack()
entry_id_cliente.place(relx=0.6, rely=0.8, anchor=tk.CENTER)

#botao do pesquisa
btn_pesquisar = tk.Button(root, text="Pesquisar", width=40, command=pesquisar_pedido)
btn_pesquisar.pack()
btn_pesquisar.place(relx=0.50, rely=0.65, anchor=tk.CENTER)
# Botão para registrar o pedido
btn_registrar = tk.Button(root, text="Registrar", width=40, command=registrar_pedido)
btn_registrar.pack()
btn_registrar.place(relx=0.50, rely=0.9, anchor=tk.CENTER)

# Botão para atualizar a tabela
""" btn_atualizar = tk.Button(root, text="Atualizar", width=40, command=atualizar_tabela)
btn_atualizar.pack()
btn_atualizar.place(relx=0.50, rely=0.95, anchor=tk.CENTER) """

# Atualizar a tabela ao iniciar o aplicativo
# Atualizar a tabela ao iniciar o aplicativo
#atualizar_tabela()


root.protocol("WM_DELETE_WINDOW", fechar_conexao)
root.mainloop()