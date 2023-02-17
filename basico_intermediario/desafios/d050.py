#Algorítimo que lê o ano de nascimento de 7 pessoas e informa quantos atingiram a maioridade:

from datetime import date
from colorama import Fore

print('informe O ano de nascimento de 7 pessoas abaixo:')
anoatual = date.today().year
maioridade = 0
minoridade = 0
print(f'{Fore.GREEN}-=' * 10)

for c in range(1, 8):
    anos = int(input(f'Pessoa {c}: '))
    if anoatual - anos >= 21:
        maioridade += 1
    else:
        minoridade += 1

print('-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'{maioridade} pessoas {Fore.GREEN}ATINGIRAM{Fore.RESET} a maioridade!!!')
print(f'{minoridade} pessoas {Fore.RED}NÃO ATINGIRAM{Fore.RESET} a maioridade!!!')