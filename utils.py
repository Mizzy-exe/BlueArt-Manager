import os
from datetime import datetime

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data_hora():
    agora = datetime.now()
    return agora.strftime('%d/%m/%Y %H:%M')             # diz a data e hora do registro da comissão

