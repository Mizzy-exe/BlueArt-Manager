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
        registro = config.data_hora()
        return registro
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

            return opcao_escolhida
            # confirm = input('Tem certeza: [S/N] ').strip().capitalize()

            # if confirm == 'S':
            #     print('Confirmado.')
            #     comissao[cliente] = {
            #         'opcao': opcao_escolhida,
            #         'data_hora': utils.data_hora()
            #     }

            #     return comissao[cliente]  # Retorna a comissão adicionada para ser salva no arquivo JSON
            # else:
            #     print('Então tente novamente.')
            #     print()
        else:
            print('Opção invalida! Tente novamente.')   
            print() 

# ta ficando bagunçado, eu tenho que fazer cada devido cliente receber no arquivo json suas escolhas e não ter dois arquivos de clientes, pelo menos pra mim não faz sentido, mas eu vou deixar assim por enquanto, depois eu vejo se mudo.

#  ja tenho uma ideia. Arrumar a funcao de adicionar comissao e chamar essa funcao dentro de add cliente, assim cada cliente vai ter suas comissoes dentro do arquivo clientes.json, e nao vai precisar de outro arquivo.
