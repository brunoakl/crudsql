import Helpers as he

class Pedido:
    def __init__(self, id: int = None, data_pedido: str = None, id_cliente: int = None, status: str = None):
        self.set_id(he.iniciar_string(id))
        self.set_data_pedido(he.iniciar_string(data_pedido))
        self.set_id_cliente(he.iniciar_inteiro(id_cliente))
        self.set_status(he.iniciar_string(status))

    def set_id(self, id_pedido: int):
        self.id = id_pedido

    def set_data_pedido(self, data_pedido: str):
        self.data_pedido = data_pedido

    def set_id_cliente(self, id_cliente: int):
        self.id_cliente = id_cliente

    def set_status(self, status: str):
        self.status = status

    def get_id(self):
        return self.id

    def get_data_pedido(self):
        return self.data_pedido

    def get_id_cliente(self):
        return self.id_cliente

    def get_status(self):
        return self.status
