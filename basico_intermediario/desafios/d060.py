#Algorítimo que lê vários números, realiza a soma entre eles e só para quando o usuário digitar 999:

from colorama import Fore
from time import sleep

print(f'Programa que lê quantos números o usuário queira e realiza a soma entre eles. Programa so para quando usuário digitar {Fore.RED}999.')
cont = 1
soma = 0
numero = 0

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
while numero != 999:
    numero = float(input(f'Informa o Número {Fore.GREEN}{cont} [999 para parar]:{Fore.RESET} '))
    if numero != 999:
        cont += 1
        soma += numero

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print(f'{Fore.GREEN}Programa Encerrado!!!')
print(f'CALCULANDO SOMATÓRIO...{Fore.RESET}')
sleep(2)
print(f'O somatório dos {Fore.CYAN}{cont - 1}{Fore.RESET} números informados foi igual à: {Fore.CYAN}{soma:.2f}{Fore.RESET}')