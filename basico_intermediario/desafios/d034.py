#Algorítimo que checa entre dois número qual é o maior e menor, ou se os dois valores são igual:
from colorama import Fore

print(f'{Fore.MAGENTA}------------------------------------------------------------------------------------{Fore.RESET}')
print('Informe dois valores para checar qual é o maior e menor, ou se os dois são iguais:')
n1 = float(input(f'{Fore.RED}Número 1: '))
n2 = float(input(f'{Fore.BLUE}Número 2: '))

if n1 > n2:
    print(f'{Fore.RESET}O número {Fore.RED}{n1}{Fore.RESET} é {Fore.GREEN}MAIOR{Fore.RESET} que o número {Fore.BLUE}{n2}{Fore.RESET}')
elif n2 > n1:
    print(f'{Fore.RESET}O número {Fore.RED}{n1}{Fore.RESET} é {Fore.GREEN}MENOR{Fore.RESET} que o número {Fore.BLUE}{n2}{Fore.RESET}')
else:
    print(f'{Fore.RESET}O número {Fore.RED}{n1}{Fore.RESET} é {Fore.GREEN}IGUAL{Fore.RESET} ao número {Fore.BLUE}{n2}{Fore.RESET}')
print(f'{Fore.MAGENTA}------------------------------------------------------------------------------------{Fore.RESET}')
