#Algorítimo que verifica se 3 retas podem formar um triângulo

import colorama
from colorama import Fore, Back, Style
colorama.init()

print('\033[35mPor favor, informa os 3 valores de retas a baixo')
r1 = float(input(f'{Fore.RED}Reta 1: '))
r2 = float(input(f'{Fore.GREEN}Reta 2: '))
r3 = float(input(f'{Fore.BLUE}Reta 3: '))
condiçao = (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2)
if condiçao == True:
    print(f'{Fore.RESET}Os lados \033[4m{Fore.RED}{r1}{Fore.RESET}\033[m, \033[4m{Fore.GREEN}{r2}{Fore.RESET}\033[m, \033[4m{Fore.BLUE}{r3}{Fore.RESET}\033[m PODEM formam um triângulo!!!')
else:
    print(f'Os lados \033[4m{Fore.RED}{r1}{Fore.RESET}\033[m, \033[4m{Fore.GREEN}{r2}{Fore.RESET}\033[m, \033[4m{Fore.BLUE}{r3}{Fore.RESET}\033[m NÃO PODEM formam um triângulo!!!')
print(f'{Fore.CYAN}---FIM---{Fore.RESET}')