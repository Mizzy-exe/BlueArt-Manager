import arquivo
from datetime import datetime

def faturamento():
    print('\n--- FATURAMENTO DO DIA ---')

    # with open('clientes.json', 'r', encoding='utf-8') as arquivo:
    #     dicionario = json.load(arquivo)

    dicionario = arquivo.json_simples('clientes.json')

    dia = datetime.now().strftime('%d/%m/%Y')
    soma_faturamento = 0.0
 
    for nome, info in dicionario.items():
        if info["data"] == dia:
            soma_faturamento += info['opcao']['brl']

    print(f'Faturamento do dia {dia}: R$ {soma_faturamento:.2f}')


def faturamento_mes():
    print('\n--- FATURAMENTO DO MÊS ---')

    dicionario = arquivo.json_simples('clientes.json')

    mes = datetime.now().strftime('%m/%Y')
    soma_faturamento = 0.0

    for nome, info in dicionario.items():
        if info["data"][3:] == mes:
            soma_faturamento += info['opcao']['brl']

    print(f'Faturamento do mês {mes}: R$ {soma_faturamento:.2f}')