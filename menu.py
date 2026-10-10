from time import sleep
import cliente
import comissao
import faturamento

def menu_principal():
    tam = 40

    opcoes = {
        '1': 'Menu de Clientes',
        '2': 'Menu de Comissões',
        '3': 'Menu de Faturamento',
        '4': 'Menu de Configuração',
        '0': 'Sair'
    }


    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"BLUEART MANAGER":^{tam}}|')
        print(f'+{"-" * tam}+')

        for i, j in opcoes.items():
            print(f'|{f" {i} - {j}":<{tam}}|')
        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op not in opcoes:
            print('Opção inválida')
            continue

        if op == '0':
            break

        print(f'>>> {opcoes[op]}\n')

        match op:
            case '1':
                menu_cliente()

            case '2':
                menu_comissoes()

            case '3':
                menu_faturamento()


def menu_cliente():
    tam = 40

    opcoes = {
        '1': 'Adicionar',
        '2': 'Listar',
        '3': 'Editar',
        '4': 'Pesquisar',
        '5': 'Excluir',
        '0': 'Sair'
    }


    while True:
        print(f'+{"-" * tam}+')
        print(f'|{"CLIENTES":^{tam}}|')
        print(f'+{"-" * tam}+')

        for i, j in opcoes.items():
            print(f'|{f" {i} - {j}":<{tam}}|')
        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op not in opcoes:
            print('Opção inválida')
            continue

        if op == '0':
            break

        print(f'>>> {opcoes[op]}\n')

        match op:
            case '1':
                cliente.add_cliente()

            case '2':
                cliente.listar_clientes()

            case '3':
                cliente.editar_cliente()

            case '4':
                cliente.pesquisar_cliente()

            case '5':
                cliente.excluir_cliente()
                



# def menu_clientes():
#     print('-' * 40)
#     print(f'{"MENU CLIENTES":^40}')
#     print('-' * 40)

#     lista = []

#     print('[1] Adicionar cliente')
#     print('[2] Listar clientes')
#     print('[3] Editar cliente')
#     print('[4] Pesquisar cliente')
#     print('[5] Excluir cliente')
#     print('[0] Voltar ao menu principal')

#     resposta = input('Escolha uma opção: ').strip()
#     if resposta == '0':
#         return
#     elif resposta == '1':
#         cliente.add_cliente()
#     elif resposta == '2':  
#         sleep(1)
#         cliente.listar_clientes('clientes.json')
#         print()
#     elif resposta == '3':
#         sleep(1)
#         cliente.editar_cliente('clientes.json')
#     elif resposta == '4':
#         sleep(1)
#         cliente.pesquisar_cliente('clientes.json')
#     elif resposta == '5':
#         sleep(1)
#         cliente.excluir_cliente('clientes.json')
#     menu_clientes()


def menu_comissoes():
    print('-' * 40)
    print(f'{"MENU COMISSÕES":^40}')
    print('-' * 40)

    print('[1] Ver comissões em andamento')
    print('[2] Ver comissões pendentes')
    print('[3] Ver comissões finalizadas')
    print('[4] ver comissões canceladas')
    print('[5] Mudar status de comissão')
    print('[0] Voltar ao menu principal')

    resposta = input('Escolha uma opção: ').strip()

    if resposta == '0':
        return
    elif resposta == '1':
        sleep(1)
        comissao.listar_comissoes_por_status('Em andamento')
    elif resposta == '2':
        sleep(1)
        comissao.listar_comissoes_por_status('Pendente')
    elif resposta == '3':
        sleep(1)
        comissao.listar_comissoes_por_status('Finalizada')
    elif resposta == '4':
        sleep(1)
        comissao.listar_comissoes_por_status('Cancelada')
    elif resposta == '5':
        sleep(1)
        comissao.mudar_status_comissao()
    else:
        print('Opção inválida. Voltando ao menu principal...')
        sleep(2)
        return


def menu_faturamento():
    print('-' * 40)
    print(f'{"MENU FATURAMENTO":^40}')
    print('-' * 40)

    print('[1] Ver faturamento do dia')
    print('[2] Ver faturamento do mês')
    print('[0] Voltar ao menu principal')

    resposta = input('Escolha uma opção: ').strip()

    if resposta == '0':
        return
    elif resposta == '1':
        sleep(1)
        faturamento.faturamento()
    elif resposta == '2':
        sleep(1)
        faturamento.faturamento_mes()
    else:
        print('Opção inválida. Voltando ao menu principal...')
        sleep(2)
        return 
    