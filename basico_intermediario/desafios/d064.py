#Jogo de Par ou Ímpar contra o computador. Programa so encerra se o PC ganhar:

from random import randint
from colorama import Fore
from time import sleep

print('Bem vindo ao jogo de Par ou Ímpar contra o Computador!! O programa so encerra quando o jogador perde.')
vitorias = 0

while True:
    print(f'{Fore.MAGENTA}-=' * 20)
    print(f'{Fore.RESET}', end='')
    escolha = input(f'Jogador, qual sua escolha, {Fore.GREEN}"PAR" ou "IMPAR"{Fore.RESET}? ').strip().upper()[0]
    while escolha != 'P' and escolha != 'I':
         print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite novamente.{Fore.RESET}')
         escolha = input(f'Jogador, qual sua escolha, {Fore.GREEN}"PAR" ou "IMPAR"{Fore.RESET}? ').strip().upper()[0]

    numero = int(input('Jogador, qual seu número de escolha de 0 a 10? '))
    while numero < 0 or numero > 10:
        print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite novamente.{Fore.RESET}')
        numero = int(input(f'Jogador, qual seu {Fore.GREEN}NÚMERO{Fore.RESET} de escolha? '))

    print(f'{Fore.MAGENTA}-=' * 20)
    print(f'{Fore.RESET}', end='')
    numeropc = randint(0, 10)
    vencedor = (numero + numeropc) % 2
    if escolha == 'P':
        if vencedor == 0:
            print(f'{Fore.GREEN}O JOGADOR VENCEU!{Fore.RESET} O número escolhido pelo computador foi {Fore.RED}{numeropc}{Fore.RESET}')
            print(f'A soma entre o número escolhido pelo jogador {Fore.GREEN}({numero}){Fore.RESET} e o número escolhido pelo computador {Fore.RED}({numeropc}){Fore.RESET} é PAR!')
            print('Com a vitória do jogador, o programa irá continuar!!')
            vitorias += 1
            sleep(2)
        elif vencedor == 1:
            print(f'{Fore.RED}O COMPUTADOR VENCEU!{Fore.RESET} O número escolhido pelo computador foi {Fore.GREEN}{numeropc}{Fore.RESET}')
            print(f'A soma entre o número escolhido pelo jogador {Fore.GREEN}({numero}){Fore.RESET} e o número escolhido pelo computador {Fore.RED}({numeropc}){Fore.RESET} é ÍMPAR!')
            print('Com a vitória do computador o programa será encerrado. Obrigado por jogar!!')
            sleep(2)
            break
    elif escolha == 'I':
        if vencedor == 1:
            print(f'{Fore.GREEN}O JOGADOR VENCEU!{Fore.RESET} O número escolhido pelo computador foi {Fore.RED}{numeropc}{Fore.RESET}')
            print(f'A soma entre o número escolhido pelo jogador {Fore.GREEN}({numero}){Fore.RESET} e o número escolhido pelo computador {Fore.RED}({numeropc}){Fore.RESET} é ÍMPAR!')
            print('Com a vitória do jogador, o programa irá continuar!!')
            sleep(2)
            vitorias += 1
        elif vencedor == 0:
            print(f'{Fore.RED}O COMPUTADOR VENCEU!{Fore.RESET} O número escolhido pelo computador foi {Fore.GREEN}{numeropc}{Fore.RESET}')
            print(f'A soma entre o número escolhido pelo jogador {Fore.GREEN}({numero}){Fore.RESET} e o número escolhido pelo computador {Fore.RED}({numeropc}){Fore.RESET} é PAR!')
            print('Com a vitória do computador o programa será encerrado. Obrigado por jogar!!')
            sleep(2)
            break

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print(f'O jogador conseguiu conquistar {Fore.GREEN}{vitorias}{Fore.RESET} vitórias até perder!!!')
