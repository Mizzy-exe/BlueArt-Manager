import json
import os
import config
import arquivo
from time import sleep
import menu
import utils

print('-' * 40)
print(f'{"BEM-VINDO AO SISTEMA DE COMISSÕES":^40}')
print('-' * 40)

if os.path.exists('config.json'):                                   # Verifica se o arquivo de configuração existe
    with open('config.json', 'r', encoding='utf-8') as arquivo:
        artista = json.load(arquivo)
    print(f'Arquivo encontrado! Bem vindo(a) {artista['nome_artistico']}')
else:
    print('Nada foi encontrado. Criando um novo arquivo...')
    sleep(2)
    artista = config.config_artista()
    arquivo.salvar_config(artista)
    arquivo.exibir_json(artista)

sleep(3)
utils.limpar_terminal()                   

sleep(1)
print()
print(f'            ---{artista['nome_artistico']}---'.upper())

menu.menu_principal()
utils.limpar_terminal()
menu.menu_clientes()



# while True:
#     opcao = config.tabela_esc()
#     registro = comissao.extra(opcao)

#     print(f'Comissão registrada em {registro}')
#     print()
    
#     continuar = input('Deseja registrar outra comissão? [S/N]: ').strip().capitalize()

#     if continuar != 'S':
#         print('Encerrando o sistema de comissões... Até logo!')
#         break
