--Tabela de clientes
CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereço VARCHAR(99) NOT NULL
);

-- Tabela de pedidos
CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    data_pedido DATE NOT NULL,
    id_cliente INT,
    status VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

--Inserir um pedido
INSERT INTO Pedidos (id_pedido, data_pedido, id_cliente, status)
VALUES ('P001', '2023-06-26', 1, 'Pendente');

--Listar todos os pedidos
SELECT * FROM Pedidos;

--Ler um pedido específico
SELECT * FROM Pedidos WHERE id = 1;

--Atualizar um pedido para "Entregue"
UPDATE Pedidos SET status = 'Entregue' WHERE id = 1;

--Excluir um pedido
DELETE FROM Pedidos WHERE id = 1; --O id do pedido a excluir