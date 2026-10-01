from time import sleep
import config

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


def add_comissao():
    print('\n--- ADICIONAR COMISSÃO ---')

    # continuar daqui para adicionar a função de adicionar comissão, que vai ser bem parecida com a função de adicionar cliente, mas com mais campos e mais complexa.
