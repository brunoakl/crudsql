import Helpers as he

class cliente:
    def __init__(self, id:int = None, nome:str = None, telefone:str=None,endereço:str=None) -> None:
        self.set_id(he.iniciar_inteiro(id))
        self.set_nome(he.iniciar_string(nome))
        self.set_telefone(he.iniciar_string(telefone))
        self.set_endereço(he.iniciar_string(endereço))
    
        
    def set_id(self,id:int):
        self.id = id
    
    def set_nome(self,nome:str):
        self.nome = nome
        
    def set_telefone(self,telefone:str):
        self.telefone=telefone
        
    def set_endereço(self,endereço:str):
        self.endereço=endereço
        
        
        
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_telefone(self):
        return self.telefone

    def get_endereco(self):
        return self.endereço
