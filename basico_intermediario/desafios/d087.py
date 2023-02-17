from datetime import date

dados = dict()

dados['Nome'] = str(input('Qual seu nome: '))
nascimento = int(input('Qual seu nome de nascimento: '))
dados['Idade'] = date.today().year - nascimento
carteira = int(input('Carteira de Trabalho (0 não tem): '))
dados['CTPS'] = carteira
if carteira != 0:
    dados['Contratação']  = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Qual seu salário: R$'))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - nascimento
print('=-' * 30)
print(dados)
for keys, values in dados.items():
    print(f'{keys} tem o valor {values}.')
print('=-' * 30)