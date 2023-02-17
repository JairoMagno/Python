#Algorítimo que faz a contagem regressiva de 10 até paras os fogos de artifício do ano novo:

from time import sleep
from colorama import Fore
from emoji import emojize

print(f'{Fore.BLUE}Está na hora da cotagem regressiva para o ano novo!!! CONTE COMIGO!!!')
print('-=' * 10)
sleep(1)
for c in range(10, -1, -1):
    print(f'{c}')
    sleep(1)
sleep(1)
print('-=' * 10)
print(emojize(f'{Fore.GREEN}BUUUUMMM! FELIZ ANO NOVO!!!!{Fore.RESET} :glowing_star::fireworks::glowing_star:'))