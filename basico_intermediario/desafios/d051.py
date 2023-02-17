#Algorítimo que lê peso de pessoas e informa quem pesa mais e quem pesa menos:

from colorama import Fore

quantidade = int(input('Informa quantas pessoas será verificado o seu peso: '))
maior = 0
menor = 0

print(f'{Fore.GREEN}-=' * 10)

for c in range(1, quantidade + 1):
    peso = float(input(f'Pessoa {c}: Kg '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'A pessoa mais {Fore.CYAN}PESADA{Fore.RESET} pesa {Fore.CYAN}{maior:.2f}Kg{Fore.RESET}.')
print(f'A pessoa mais {Fore.MAGENTA}LEVE{Fore.RESET} pesa {Fore.MAGENTA}{menor:.2f}Kg{Fore.RESET}.')