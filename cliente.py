import os
from time import sleep
import utils, menu, comissao, arquivo, json, arquivo

def add_cliente():
    if os.path.exists('clientes.json'):                                 # checa se o arquivo clientes.json existe
        with open('clientes.json', 'r', encoding='utf-8') as arquivo:
            clientes = json.load(arquivo)
        print(f'--- Arquivo encontrado! {len(clientes)} clientes carregados. ---')
    else:
        clientes = {}
        print('--- Nenhum arquivo encontrado. Criando nova lista. ---')

    while True:                                                         #loop para adicionar clientes
        print()
        print('\n--- ADICIONAR NOVO CLIENTE ---')
        nome = input('Nome do cliente (ou "sair"): ').capitalize().strip()

        if nome.lower() == 'sair':
            break

        sexo = input('Sexo (F/M): ').capitalize().strip()
        if sexo not in 'FM':
            sexo = input('Tente novamente. Sexo (F/M): ').capitalize().strip()

        idade = int(input('idade: '))
        if idade < 18:
            print('Por favor, informe o número do seu responsável.')

        celular = input('Numero de celular: ')
        email = input('Email: ').capitalize().strip()
        cidade = input('Cidade: ').capitalize().strip()

        opcao = comissao.add_comissao(nome)

        comfirm = input('Tem certeza que deseja adicionar este cliente? [S/N]: ').strip().capitalize()
        print()
        
        if comfirm == 'S':
            print(f'Cliente {nome} adicionado com sucesso!')
        
            clientes[nome] = {
                'sexo': sexo,
                'idade': idade,
                'celular': celular,
                'email': email,
                'cidade': cidade,
                'opcao': opcao,
                'data_hora': utils.data_hora()
        }

            with open('clientes.json', 'w', encoding='utf-8') as arquivo:                  # faz a atualização do arquivo clientes.json com os novos dados
                    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

            print()
            print('--- Cliente adicionado ---')
            print(f'Agora temos {len(clientes)} clientes cadastrados.')
            return clientes

        else:
            print('Cliente não adicionado. Voltando ao menu principal...')
            sleep(2)
            return menu.menu_principal()

def listar_clientes(clientes):                              # lista todos os clientes cadastrados no arquivo clientes.json
    print('\n--- LISTA DE CLIENTES ---')

    dicionario = arquivo.json_simples(clientes)

    for nome, info in dicionario.items():
        print(f'Nome: {nome}')
        print(f'Sexo: {info["sexo"]}')
        print(f'Idade: {info["idade"]}')
        print(f'Celular: {info["celular"]}')
        print(f'Email: {info["email"]}')
        print(f'Cidade: {info["cidade"]}')
        print('-' * 30)


def editar_cliente(clientes):
    print('\n--- EDITAR CLIENTE ---')

    with open ('clientes.json', 'r', encoding='utf-8') as arquivo:
        dicionario = json.load(arquivo)
        
    nome = input('Digite o nome do cliente que deseja encontrar: ').capitalize().strip()

    if nome in dicionario:
        print(f'Cliente encontrado: {nome}')

        print()
        print('>>> INFORMAÇÕES ATUAIS')
        print()

        print(f'Nome: {nome}')
        print(f'Sexo: {dicionario[nome]["sexo"]}')
        print(f'idade: {dicionario[nome]["idade"]}')
        print(f'Celular: {dicionario[nome]["celular"]}')
        print(f'Email: {dicionario[nome]["email"]}')
        print(f'Cidade: {dicionario[nome]["cidade"]}')

        print()
        campo = input('Escreva qual campo deseja editar (nome, sexo, idade, celular, email, cidade): ').lower().strip()

        if campo in dicionario[nome]:
            novo_valor = input(f'Novo valor para {campo}: ')
            dicionario[nome][campo] = novo_valor

            with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)


def pesquisar_cliente(clientes):
    print('\n--- PESQUISAR CLIENTE ---')

    dicionario = arquivo.json_simples(clientes)

    nome = input('Digite o nome do cliente que deseja encontrar: ').capitalize().strip()
    print()
    if nome in dicionario:
        for i, j in dicionario[nome].items():
            print(f'{i.capitalize()}: {j}')
    else:
        print('Cliente não encontrado.')


def excluir_cliente(clientes):
    print('\n--- EXCLUIR CLIENTE ---')

    with open ('clientes.json', 'r', encoding='utf-8') as arquivo:
            dicionario = json.load(arquivo)

    nome = input('Digite o nome do cliente que deseja excluir: ').capitalize().strip()

    if nome in dicionario:
        confirmacao = input(f'Tem certeza que deseja excluir {nome}? (S/N): ').strip().upper()

        if confirmacao == 'S':
            del dicionario[nome]
            print(f'Cliente {nome} excluído com sucesso.')

            with open('clientes.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)

        else:
            print('Exclusão cancelada.')

