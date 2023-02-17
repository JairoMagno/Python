#Algorítimo que calcula a tabuada de um valor e pergunta ao usuário se quer ver de outro número. Condição de parada é um valor negativo:

from colorama import Fore
cont = 1

while True:

    print(f'{Fore.MAGENTA}-=' * 20)
    print(f'{Fore.RESET}', end='')
    n = int(input(f'Quer ver a tabuada de qual valor {Fore.GREEN}[Digite número negativo para parar]:{Fore.RESET} '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n * cont}')
        cont += 1
    cont = 1
print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print(f'{Fore.GREEN}NÚMERO NEGATIVO PRESSIONADO!!. Programa Finalizado, obrigado por participar!{Fore.RESET}')
