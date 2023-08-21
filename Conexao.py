import psycopg2



class ErroBancoNaoExiste(Exception):
    """Erro ao conectar ao banco de dados."""
    pass

class ErroConexao(Exception):  
    """Erro ao conectar ao banco de dados."""
    pass

class ErroConsulta(Exception): 
    """Erro ao consultar o banco de dados."""
    pass

class ErroExecucao(Exception):
    """Erro ao executar o comando."""
    pass

class Conexao:
    """Classe de conexão com o banco de dados."""
    def __init__(self, nome_banco: str, usuario: str, senha: str, host: str = "localhost"):
        """Construtor da classe Conexao."""
        try:
            self.conexao = psycopg2.connect(
                host=host,
                database=nome_banco,
                user=usuario,
                password=senha
            )
            self.cursor = self.conexao.cursor()
        except Exception as E:
            if  "does not exist" in E.args[0]:
                raise ErroBancoNaoExiste("Banco de dados não existe.")
            else:
                raise ErroConexao("Erro ao conectar ao banco de dados.")
        
    def executar(self, sql: str):
        """Executa um comando SQL."""
        try:
            self.cursor.execute(sql)
            self.conexao.commit()
        except:
            self.conexao.rollback()
            raise ErroExecucao("Erro ao executar o comando.")

    def consultar(self, sql: str):
        """Executa um comando SQL e retorna o resultado."""
        consulta = None
        try:
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()
        except Exception as E:
            self.conexao.rollback()  
            raise ErroConsulta("Erro ao consultar o banco de dados. \n\n" + str(E))
        return consulta  

    def fechar(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.conexao.close()
