#Algorítimo de tabuada V2.0:

from time import sleep
from colorama import Fore

numero = float(input('Escolha o número que você deseja calcular a tabuada: '))
print('Número escolhido! CALCULANDO...')
sleep(2)
resultado = 0
print(f'{Fore.GREEN}-=' * 10)

for c in range(1, 11):
    resultado = numero * c
    print(f'{numero} X {c} = {resultado}')

print('-=' * 10, end='')
print(f'{Fore.RESET}')
