from time import sleep
import cliente
import comissao

def menu_principal():
    while True:
        print('-' * 40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-' * 40)

        print('[1] Clientes')
        print('[2] Comissões')
        print('[3] Histórico')
        print('[4] Faturamento')
        print('[5] Configurações')
        print('[0] Sair')

        resposta = input('Escolha uma opção: ').strip()
        if resposta == '0':
            print('Encerrando o sistema de comissões... Até logo!')
            sleep(2)
            break
        if resposta == '1':
            sleep(1)
            menu_clientes()
        elif resposta == '2':
            sleep(1)
            menu_comissoes()



def menu_clientes():
    print('-' * 40)
    print(f'{"MENU CLIENTES":^40}')
    print('-' * 40)

    lista = []

    print('[1] Adicionar cliente')
    print('[2] Listar clientes')
    print('[3] Editar cliente')
    print('[4] Pesquisar cliente')
    print('[5] Excluir cliente')
    print('[0] Voltar ao menu principal')

    resposta = input('Escolha uma opção: ').strip()
    if resposta == '0':
        return
    elif resposta == '1':
        cliente.add_cliente()
    elif resposta == '2':  
        sleep(1)
        cliente.listar_clientes('clientes.json')
        print()
    elif resposta == '3':
        sleep(1)
        cliente.editar_cliente('clientes.json')
    elif resposta == '4':
        sleep(1)
        cliente.pesquisar_cliente('clientes.json')
    elif resposta == '5':
        sleep(1)
        cliente.excluir_cliente('clientes.json')
    menu_clientes()


def menu_comissoes():
    print('-' * 40)
    print(f'{"MENU COMISSÕES":^40}')
    print('-' * 40)

    print('[1] Ver comissões em andamento')
    print('[2] Ver comissões pendentes')
    print('[3] Ver comissões finalizadas')
    print('[4] ver comissões canceladas')
    print('[5] Status das comissões')
    print('[6] Mudar status de comissão')
    print('[0] Voltar ao menu principal')

    resposta = input('Escolha uma opção: ').strip()

    if resposta == '0':
        return
    elif resposta == '1':
        sleep(1)

       