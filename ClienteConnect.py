import Conexao
import clientes
import Helpers


class connect (Conexao.Conexao):
    def __init__(self,cliente:clientes.cliente=None):
        super().__init__(nome_banco="postgres", usuario="postgres", senha="1234")
        self.set_clientes(Helpers.iniciar_var(cliente))
    
    def set_clientes(self,clientes:clientes.cliente):
        self.cliente=clientes
        return self
        
    def Criar_cliente(self):
        sql="""INSERT INTO Clientes (id, nome, telefone, endereço)
        VALUES (%s, '%s','%s','%s');""" %(self.cliente.get_id(),
                                          self.cliente.get_nome(),
                                          self.cliente.get_telefone(),
                                          self.cliente.get_endereco())
        
        self.executar(sql)
        self.fechar()
        
    def Read_cliente(self,codigo):
        sql="SELECT * FROM Clientes WHERE id = %s"%(str(codigo))
        
        return self.consultar(sql)
        
        
    def Update_cliente(self):
        sql="UPDATE Clientes SET (nome='%s', telefone='%s', endereço='%s') WHERE id = %s "%(self.cliente.get_nome(), 
        self.cliente.get_telefone(), 
        self.cliente.get_endereco(),
        self.cliente.get_id())
        
        self.executar(sql)
        self.fechar()
        
        
    def Delete_cliente(self,codigo:int):
        sql="DELETE FROM Clientes WHERE id = %s"%(str(codigo))
        
        self.executar(sql)
        self.fechar()
        
    
        