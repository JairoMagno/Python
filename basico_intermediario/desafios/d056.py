#Algorítimo que calcula o fatorial de um número:

from colorama import Fore

numero = int(input('Escolha o número que você quer calcular o fatorial: '))
contagem = numero
fatorial = 1

print(f'{Fore.MAGENTA}-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'O fatorial de {numero}! = ', end='')
while contagem > 0:
    fatorial *= contagem
    print(f'{contagem}', end='')
    print(' x ' if contagem > 1 else ' = ', end='')
    contagem -= 1
print(f'{fatorial}')
print(f'{Fore.MAGENTA}-=' * 10, end='')
print(f'{Fore.RESET}')