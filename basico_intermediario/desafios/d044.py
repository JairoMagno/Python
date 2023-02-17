#Algorítimo que calcula a soma de entre todos números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500:

from time import sleep
from colorama import Fore

print('Será feito a conta de todos os números ímpares e múltiplos de 3 no intervalo de 1 a 500:')
print('CALCULANDO...')
sleep(1)
soma = 0
print(f'{Fore.GREEN}-=' * 10)
for c in range(1, 501, 2):
    if (c % 3 == 0):
        print(f'{c}', end=' ')
        soma += c

print('\n', end='')
print('-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'A soma total desses valores é de {soma}.')