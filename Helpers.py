from tkinter import filedialog as file, messagebox as msg
from os.path import exists
import os
import tkinter as tk
from tkinter import ttk
import datetime

class ErroSalvarArquivo(Exception):
    """Exceção para quando ocorrer um erro ao salvar um arquivo"""
    pass
class ErroAbrirArquivo(Exception):
    """Exceção para quando ocorrer um erro ao abrir um arquivo"""
    pass

def mensagem(titulo: str, mensagem: str):
    """Exibe uma mensagem, Titulo sendo o nome da janela e Mensagem o texto exibido"""
    msg.showinfo(titulo, mensagem, icon=msg.INFO)

def validar_data(data: str):
    """Verifica se a data informada é válida, caso seja, retorna True, caso não seja, retorna False"""
    try:
        datetime.datetime.strptime(data, 'mm/dd/YYYY')
        return True
    except:
        return False

def achar_arquivo(caminho: str):
    return exists(caminho)

def abrir_arquivo_ini(caminho: str):
    arquivo = os.path.abspath(caminho)
    import configparser
    config = configparser.ConfigParser()
    config.read(arquivo)
    return config['BANCO']

def salvar_arquivo_ini(caminho: str, dados: dict):
    import configparser
    config = configparser.ConfigParser()
    config['BANCO'] = dados
    with open(save_file(tipos= (('Arquivos Ini', '*.ini'), ('Arquivos Ini', '*.ini')), 
                        nome=caminho), 'w') as configfile:
        config.write(configfile)

def iniciar_var(variavel, default = None):
    """Iniciar uma variavel, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve None"""
    if variavel is None:
        variavel = default
    else:
        variavel = variavel
    return variavel

def iniciar_time(tempo: datetime.time, default: datetime.time = datetime.time(0, 0, 0)):
    """Iniciar uma variavel do tipo Time, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve '00:00:00'"""
    return iniciar_var(tempo, default)

def iniciar_date(data: datetime.date, default: datetime.date = datetime.date.today()):
    """Iniciar uma variavel do tipo Date, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve a data atual"""
    return iniciar_var(data, default)

def iniciar_string(string: str, default: str = ""):
    """Iniciar uma variavel do tipo String, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve uma string vazia"""
    return iniciar_var(string, default)

def iniciar_inteiro(inteiro: int, default: int = 0):
    """Iniciar uma variavel do tipo Inteiro, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve 0"""
    return iniciar_var(inteiro, default)

def iniciar_float(float: float, default: float = 0.0):
    """Iniciar uma variavel do tipo Float, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve 0.0"""
    return iniciar_var(float, default)

def iniciar_boolean(boolean: bool, default: bool = False):
    """Iniciar uma variavel do tipo Booleano, caso ela seja None, devolve o valor default informado,
       caso não seja informado devolve False"""
    return iniciar_var(boolean, default)
    
def str_to_int_def(string: str, default: int = 0):
    """Converte uma string para inteiro, caso não seja possivel, retorna o ValorPadrao informado,
       caso não seja informado devolve 0"""
    try:
        return int(string)
    except:
        return default

def if_then(condicao: bool, true_value, false_value):
    """Verifica se a condição é verdadeira, caso seja, retorna TrueValue, caso não seja, retorna FalseValue"""
    if condicao:
        return true_value
    else:
        return false_value

def bring_to_front(form: tk.Toplevel):
    """Traz o formulario informado para frente"""
    form.attributes('-topmost', True)
    form.attributes('-topmost', False)

def max_size(string: tk.StringVar, size: int, *args):
    """Verifica se o texto informado é maior que o tamanho informado,
       caso seja, retorna o texto cortado, caso não seja, retorna o texto"""
    texto = string.get()
    if len(texto) > size:
        texto = string.get()[:size]
    string.set(texto)

def convert_date_eng_to_pt(date: str):
    """Converte uma data no formato ingles para o formato portugues"""
    return date[6:] + '/' + date[4:6] + '/' + date[:4]   

def convert_date_pt_to_eng(date: str):
    """Converte uma data no formato portugues para o formato ingles"""
    return date[6:] + '-' + date[3:5] + '-' + date[:2]

def to_hour_format(string: tk.StringVar):
    """Verifica se o texto informado é um horario, caso seja, retorna o texto formatado,
       caso não seja, retorna o texto"""
    texto = string.get()
    if len(texto) == 1:
        texto = '0' + texto + ':00'
    elif len(texto) == 2:
        texto = texto + ':00'
    elif len(texto) == 3:
        texto = '0' + texto[0] + ':' + texto[1:]
    elif len(texto) == 4:
        texto = texto[0:2] + ':' + texto[2:]
    elif len(texto) >= 5:
        texto = texto[0:2] + ':' + texto[2:4]
    string.set(texto)

def constraint_max_length(string: tk.StringVar, size: int):
    string.trace_add('write', lambda *args: max_size(string, size))

def only_numbers(string: str):
    """Verifica se o texto informado é um numero, caso seja, retorna True, caso não seja, retorna False"""
    if str.isdigit(string) or string == "":
        return True
    else:
        return False

def constraint_only_numbers(entry: tk.Entry):
    """Define que o Entry informado só aceita numeros"""
    Constraint_OnlyNumbers = (entry.register(only_numbers))
    entry.config(validate='key', validatecommand=(Constraint_OnlyNumbers, '%P')) 

def centralize(frame: tk.Tk, largura: int, altura: int):
    """Centraliza o Frame informado na tela, Largura e Altura são as dimensões do Frame"""
    largura_tela = frame.winfo_screenwidth()
    altura_tela = frame.winfo_screenheight()   
    posicao_x = (largura_tela/2) - (largura/2)
    posicao_y = (altura_tela/2) - (altura/2)
    frame.geometry('%dx%d+%d+%d'% (largura, altura, posicao_x, posicao_y))

def full_screen(frame: tk.Tk):
    """Define que o Frame informado ocupa toda a tela"""
    frame.attributes('-fullscreen', True)

def open_file(tipos: tuple = (('Arquivos Txt', '*.txt'), ('Arquivos Txt', '*.txt')),
                 titulo: str = 'Abrir Arquivo', diretorio: str = '/'):
    """Abre uma janela para selecionar um arquivo, caso não seja selecionado nenhum arquivo,
       retorna uma exceção, caso seja selecionado, retorna o nome do arquivo,
       Tipos_Arquivos é uma tupla com os tipos de arquivos que podem ser selecionados,
       Titulo é o nome da janela, Diretorio é o diretorio inicial da janela"""
    nome_arquivo = file.askopenfilename(
                                     title=titulo,
                                     initialdir=diretorio,
                                     filetypes=tipos
                                    )
    if not nome_arquivo:
      raise ErroSalvarArquivo('Arquivo não escolhido!')
    else:
      return nome_arquivo

def save_file(tipos: tuple = (('Arquivos Txt', '*.txt'), ('Arquivos Txt', '*.txt')),
                    titulo: str = 'Salvar Arquivo', diretorio: str = '/', nome: str = ''):
    """Abre uma janela para salvar um arquivo, caso não seja selecionado nenhum arquivo,
       retorna uma exceção, caso seja selecionado, retorna o nome do arquivo, 
       Tipos_Arquivos é uma tupla com os tipos de arquivos que podem ser selecionados,
       Titulo é o nome da janela, Diretorio é o diretorio inicial da janela""" 
    nome_arquivo = file.asksaveasfilename(
                                     title=titulo,
                                     initialdir=diretorio,
                                     filetypes=tipos,
                                     initialfile=nome
                                    )
    if not nome_arquivo:
        raise ErroSalvarArquivo('Arquivo não escolhido!')
    else:
        return nome_arquivo

def focus_first_item(tree_view: ttk.Treeview):
    """Foca o primeiro item do Treeview informado"""
    tree_view.focus_set()
    item = tree_view.get_children()
    if item:
        tree_view.focus(item[0])
        tree_view.selection_set(item[0])

def get_selected_item(tree_view: ttk.Treeview):
    """Pega o item selecionado no Treeview informado"""
    return tree_view.selection()

def get_value_from_selected_item(tree_view: ttk.Treeview, posicao: int = 0):
    """Pega o código do item selecionado no Treeview informado"""
    return tree_view.item(get_selected_item(tree_view))['values'][posicao]
