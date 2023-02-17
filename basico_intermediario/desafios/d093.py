from time import sleep
from colorama import Fore
def linha():
    print('=-' * 20)
def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if f < i:
        f -= 2
    for c in range(i, f+1, p):
        print(f'{Fore.GREEN}{c} => ', end='', flush=True)
        sleep(0.5)
    print(f'FIM{Fore.RESET}')
    sleep(1)
    linha()
def contador1():

    print('Qual será a contagem personalizada?')
    início = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        print(f'{Fore.RED}Não Existe um passo nulo. Será considerado um passo de 1 em 1{Fore.RESET}')
        passo = 1
    if fim < início and passo >= 0:
        passo *= -1
        fim -= 2
    if início == fim:
        print(f'{Fore.RED}A contagem inicial é igual ao final, portanto não haverá contagem!{Fore.RESET}')
    for c in range(início, fim+1, passo):
        print(f'{Fore.GREEN}{c} => ', end='', flush=True)
        sleep(0.5)
    print(f'FIM{Fore.RESET}')

contador(1, 10, 1)
contador(10, 0, -2)
contador1()

while True:
    linha()
    continuar = str(input(f'Deseja continuar? {Fore.RED}[S/N]{Fore.RESET} ')).strip().upper()[0]
    if continuar == 'N':
        break
    if continuar not in 'S':
        print(f'{Fore.RED}Informação inválida. Digite novamente!{Fore.RESET}')
    else:
        contador1()
linha()
