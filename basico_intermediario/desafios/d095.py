from random import randint
from time import sleep
from colorama import Fore

sorteio = list()
def sorteia():
    print('Será sorteado 5 valores e armazenados dentro de uma lista.')
    print('SORTEANDO...')
    sleep(2)
    for c in range(0, 5):
        sorteio.append(randint(1, 100))
    print(f'Sorteio realizado. A lista com os números aleatórios é {Fore.GREEN}{sorteio}{Fore.RESET}.')
def somapar():
    print('=-' * 30)
    sorteia()
    print('=-' * 30)
    print('A soma entre os valores pares sorteados será: ')
    print('Calculando...')
    sleep(2)
    soma = 0
    for c in sorteio:
        if c % 2 == 0:
            print(f'{Fore.RED}{c} => ', end='', flush=True)
            sleep(1)
            soma += c
    print(f'FIM.{Fore.RESET} Estes são os números pares, sua soma é {Fore.GREEN}{soma}{Fore.RESET}')
somapar()
