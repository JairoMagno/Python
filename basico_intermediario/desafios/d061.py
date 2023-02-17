#Algorítimo que lê vários números, realiza a soma entre eles e só para quando o usuário digitar 999:

from colorama import Fore
from time import sleep

print(f'Programa que lê quantos números o usuário queira e realiza a média entre eles.')

maior = menor = soma = denominador = 0
parada = ''
cont = 1

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
while parada != 'N':
    numero = float(input(f'Informe o Número {Fore.GREEN}{cont}:{Fore.RESET} '))
    parada = input(f'Deseja continuar digitando valores: [ {Fore.GREEN}S{Fore.RESET} | {Fore.RED}N{Fore.RESET} ]: ').strip().upper()[0]
        
    while parada != 'N' and parada != 'S':
        print('Informação não encontrada! Digite novamente uma das opções abaixo: ')
        parada = input(f'Deseja continuar digitando valores: [ {Fore.GREEN}S{Fore.RESET} | {Fore.RED}N{Fore.RESET} ]: ').strip().upper()[0]  
    if cont == 1:
        maior = numero
        menor = numero
    else: 
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    soma += numero
    cont += 1
    denominador += 1

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print(f'{Fore.GREEN}Programa Encerrado!!!')
print(f'CALCULANDO MÉDIA...{Fore.RESET}')
sleep(2)
if cont == 2:
    print(f'Como apenas {Fore.CYAN}1{Fore.RESET} único valor foi informado, sua média será ele mesmo e ele é o maior valor: {Fore.CYAN}{numero}{Fore.RESET}')
else:
    media = soma / (denominador)
    print(f'A média dos {Fore.CYAN}{cont - 1}{Fore.RESET} números informados foi igual à: {Fore.CYAN}{media:.2f}{Fore.RESET}')
    print(f'O maior número foi {Fore.GREEN}{maior}{Fore.RESET} e o menor valor foi {Fore.GREEN}{menor}{Fore.RESET}')
    