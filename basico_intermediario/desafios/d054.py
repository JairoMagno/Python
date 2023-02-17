#Algóritimo que tenta adivinhar o número que o computador gerou:

from random import randint
from colorama import Fore
from time import sleep

print('Olá eu sou o computador gerador, vamos brincar? tente adivinhar o número que pensei de 0 a 10!!!')
pc = randint(0, 10)
acertou = False
tentativas = 0
print(f'{Fore.CYAN}PENSANDO EM UM NÚMERO...')
sleep(2)
while acertou == False:
    print(f'{Fore.MAGENTA}-=' * 10)
    print(f'{Fore.RESET}', end='')
    numero = int(input('Qual número você chuta? '))

    if numero == pc:
        acertou = True
    elif numero != pc:
        if numero > pc:
            print(f'{Fore.RED}Ainda não... O número que pensei é MENOR!!{Fore.RESET}')
        elif numero < pc:
            print(f'{Fore.RED}Ainda não... O número que pensei é MAIOR!!{Fore.RESET}')
    tentativas += 1

print(f'{Fore.MAGENTA}-=' * 10)
print(f'{Fore.RESET}', end='')
print(f'{Fore.GREEN}CORRETO!!!{Fore.RESET} O computador pensou no número {Fore.GREEN}{pc}{Fore.RESET}. O usuário precisou de {Fore.RED}{tentativas}{Fore.RESET} tentativas para acertar!')
