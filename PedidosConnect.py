import Conexao
import pedidos
import Helpers


class PedidosDAO(Conexao.Conexao):
    def __init__(self,pedido:pedidos.Pedido=None):
        super().__init__(nome_banco="postgres", usuario="postgres", senha="1234")
        self.set_pedido(Helpers.iniciar_var(pedido))
        
    def set_pedido(self,pedido:pedidos.Pedido):
        self.pedido=pedido
        return self

    def Criar_pedido(self):
        sql = """INSERT INTO Pedidos (id, data_pedido, id_cliente, status)
                 VALUES (default, '%s', %s, '%s')""" %(self.pedido.get_data_pedido(),
                                                     self.pedido.get_id_cliente(),
                                                     self.pedido.get_status())

        self.executar(sql)
        self.fechar()

    
    def Read_pedido(self):
        sql = """select p.id, p.data_pedido, p.status, c.id, c.nome, c.endereço, c.telefone from pedidos p join clientes c on p.id_cliente = c.id"""
        return self.consultar(sql)


    def Update_pedido(self):
        sql = """UPDATE Pedidos set data_pedido = '%s',
                 id_cliente = %s, status = '%s' WHERE id = %s""" % (
                                                                   self.pedido.get_data_pedido(),
                                                                   self.pedido.get_id_cliente(),
                                                                   self.pedido.get_status())

    def deletar_pedido(self, id_pedido):
        sql = "DELETE FROM Pedidos WHERE id = %s" % id_pedido

        # Executar o comando SQL para deletar o pedido do banco de dados
        # (Código para executar o comando SQL aqui)
