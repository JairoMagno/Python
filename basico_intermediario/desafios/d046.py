#Algorítimo que recebe 6 número inteiros e calcula a soma apenas entre os números pares:

from colorama import Fore


print('Digite 6 números ao seu desejo abaixo: ')
print(f'{Fore.GREEN}-=' * 10)
par = 0

for c in range(1, 7):
    numero = int(input(f'Digite o número {c}: '))
    if numero % 2 == 0:
        par += numero
print('-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'A soma entre apenas os número pares será: {par}')