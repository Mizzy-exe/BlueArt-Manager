from time import sleep
import config
from datetime import datetime
import arquivo
import os
import utils
import json

def extra(opc):                                                  # Pergunta se o cliente quer mais alguma coisa na ilustração
    print('INFORMAÇÕES EXTRAS DA COMISSÃO')                         # adicionais, como armas, fundo detalhado, animal, etc
    print('-' * 40)

    lista = ['Personagem', 'Fundo detalhado', 'Armas', 'Animal']
    extras ={}

    for c in lista:
        item = input(f'Deseja adicionar {c}? [S/N]: ').strip().upper()
        if item == 'S':
           q = int(input('Quantos: '))
           porcento = float(input('Qual porcentagem adicional? '))

           extras[c] = {
               'quant': q,
               'porcentagem': porcento
           }
        else:
            print(f'Tudo bem, sem {c}')

        print(f'\n{extras}')

    calculo_extra(opc, extras)                         # chama a função de calculo_extra para calcular o valor total da comissão
    final = input('Essa comissão foi finalizada? [S/N]: ').upper().strip()
    print()

    if final =='S':
        data = utils.data(),utils.hora()

        return data
    else:
        print('ainda em desenvolvimento a partir daqui!')
        return None                                         # return None para caso o cliente não finalize a comissão, para não dar erro no main.py


def calculo_extra(escolha, itm):                       #itm é item, eu so fiquei sem ideia para nome do parametro
    
    print()
    print('O cliente quis adicionar: ')
    soma = 0

    for nome_item, c in itm.items():                # Aqui uso o for para listar apenas o que foi escolhido com Sim
        print(f'{c['quant']} {nome_item}')

        calculo = escolha['brl'] * (c['porcentagem'] / 100)
        calculo *= c['quant']
        soma += calculo

    print()
    total = escolha['brl'] + soma
    print(f'O valor total da comissão é: R${total:.2f}')


def add_comissao(cliente):
    print(f'Veja qual opção o(a) {cliente} quer: ')
    print()

    commission = config.opcao_commBR()  
    
    # Mostra a tabela de opções toda organizada
    while True:
        print(f'{'PINTURA':<24} {'TAMANHO':<23} {'VALOR'}')
        print()

        for i, c in enumerate(commission, start=1):                                          #tabela
            print(f'{i} - {c['tipo']:<20} {c['tamanho']:<23} {c['brl']:.2f}') 
        print() 

        esc_comm = int(input('Digite aqui: '))                           #decisao

        if 1 <= esc_comm <= len(commission):
            opcao_escolhida = commission[esc_comm - 1]
            print(f'O(a) {cliente} escolheu {opcao_escolhida['tamanho']}, {opcao_escolhida['tipo']} por R${opcao_escolhida['brl']:.2f}')
            print()

            resposta = input('Deseja confirmar esta opção? [S/N]: ').strip().upper()

            if resposta == 'S':
                print(f'Opção confirmada!')
                print()
            
            return opcao_escolhida

        else:
            print('Opção invalida! Tente novamente.')   
            print() 


def status_comissao():
    stts = 'Em andamento'  # Valor padrão para status de comissão

    return stts


def mudar_status_comissao():
    print('\n--- MUDAR STATUS DA COMISSÃO ---')

    with open('clientes.json', 'r', encoding='utf-8') as arquivo:
        dicionario = json.load(arquivo)

    nome = input('Digite o nome do cliente para mudar o status da comissão: ').capitalize().strip()

    if nome in dicionario:
        cliente_info = dicionario[nome]

        print(f'Cliente: {nome}')
        print(f'Comissão atual: {cliente_info["opcao"]["tipo"]}, {cliente_info["opcao"]["tamanho"]}, R${cliente_info["opcao"]["brl"]:.2f}')
        print(f'Status atual: {cliente_info["status"]}')

        print('\nEscolha o novo status da comissão:')

        status = int(input('[1] Em andamento\n[2] Pendente\n[3] Finalizada\n[4] Cancelada\nDigite o número correspondente: '))


        if status == 1:
            cliente_info['status'] = 'Em andamento'
        elif status == 2:
            cliente_info['status'] = 'Pendente'
        elif status == 3:
            cliente_info['status'] = 'Finalizada'
        elif status == 4:
            cliente_info['status'] = 'Cancelada'
        else:
            print('Opção inválida. Voltando ao menu principal....')
            sleep(2)
            return 

        print(f'Status da comissão do cliente {nome} alterado para: {cliente_info["status"]}')

        with open('clientes.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)

    else:
        print(f'Cliente {nome} não encontrado. Voltando ao menu principal....')
        sleep(2)
        return
        
def listar_comissoes_por_status(status):
    print(f'\n--- LISTA DE COMISSÕES {status.upper()} ---')

    with open('clientes.json', 'r', encoding='utf-8') as arquivo:
        dicionario = json.load(arquivo)

    comissao_filtrada = {
        nome: info

        for nome,info in dicionario.items()
        if info.get('status') == status
    }

    for nome, info in comissao_filtrada.items():
        print(f'Nome do Cliente: {nome}')
        print(f'Comissão: {info["opcao"]["tipo"]}, {info["opcao"]["tamanho"]}, R${info["opcao"]["brl"]:.2f}')

    print(f'\nTotal de comissões {status}: {len(comissao_filtrada)}')
