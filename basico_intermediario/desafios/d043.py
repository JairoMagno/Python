#Algorítimo que mostra todos os números pares de algum intervalo que o usuário queira:

from colorama import Fore

quantidade = int(input(f'{Fore.GREEN}Até quanto você quer analisar a quantidade de números pares: '))
print('-=' * 10)
for c in range(0, quantidade + 1, 2):
        print(f'{c}', end=' ')
print('\n', end='')
print(10 * f'-=', end='')
print(f'{Fore.RESET}')
