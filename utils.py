import os
from datetime import datetime

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data():
    agora = datetime.now()
    return agora.strftime('%d/%m/%Y')                  # diz a data do registro da comissão

def hora():
    agora = datetime.now()
    return agora.strftime('%H:%M')                     # diz a hora do registro da comissão