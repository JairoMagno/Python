#Algorítimo para o jogo Pedra, Papel, Tesoura:

from colorama import Fore
from random import choice
from time import sleep

print(f'{Fore.MAGENTA}--------------COMEÇO DO JOGO-------------{Fore.RESET}')
jogador = input('Será feito um jogo de Jokenpô contra o PC. Escolha entre PEDRA, PAPEL OU TESOURA: ').strip().upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(lista)
print(f'{Fore.CYAN}JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print(f'PÔ!!!!!{Fore.RESET}')
sleep(0.5)
print(f'{Fore.GREEN}-={Fore.RESET}' * 15)
print(f'O Jogador escolheu {jogador}')
print(f'O Computador escolheu {pc}')
print(f'{Fore.GREEN}-={Fore.RESET}' * 15)
if jogador != 'PEDRA' and jogador != 'PAPEL' and jogador != 'TESOURA':
    print('Jogada não encontrada. Escolha novamente entre PEDRA, PAPEL ou TESOURA.')
elif jogador == 'PEDRA' and pc == 'TESOURA':
    print(f'O Jogador {Fore.GREEN}VENCEU{Fore.RESET} do Computador!!!')
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print(f'O Jogador {Fore.GREEN}VENCEU{Fore.RESET} do Computador!!!')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print(f'O jogador {Fore.GREEN}VENCEU{Fore.RESET} do computador!!!')
elif jogador == 'PEDRA' and pc == 'PEDRA':
    print(f'O jogador {Fore.YELLOW}EMPATOU{Fore.RESET} com o computador!!!')
elif jogador == 'TESOURA' and pc == 'TESOURA':
    print(f'O jogador {Fore.YELLOW}EMPATOU{Fore.RESET} com o computador!!!.')
elif jogador == 'PAPEL' and pc == 'PAPEL':
    print(f'O jogador {Fore.YELLOW}EMPATOU{Fore.RESET} com o computador!!!.')
elif jogador == 'PAPEL' and pc == 'TESOURA':
    print(f'O jogador {Fore.RED}PERDEU{Fore.RESET} do computador!!!')
elif jogador == 'PEDRA' and pc == 'PAPEL':
    print(f'O jogador {Fore.RED}PERDEU{Fore.RESET} do computador!!!')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print(f'O jogador {Fore.RED}PERDEU{Fore.RESET} do computador!!!')
print(f'{Fore.MAGENTA}----------------FIM DO JOGO--------------{Fore.RESET}')
