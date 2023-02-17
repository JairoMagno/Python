from colorama import Fore

linha = '=' * 50
titulo = 'LISTAGEM DE PREÇOS'
print(f'{Fore.GREEN}{linha}')
print(titulo.center(50))
print(f'{linha}{Fore.RESET}')

tupla = ('Playstation 1', 250, 'Playstation 2', 500, 'Playstation 3', 1000, 'Playstation 4', 2000, 'Playstation 5', 5000) 

for posição in range(0, len(tupla)):
    if posição % 2 == 0:
        print(f'{tupla[posição]:.<35}', end='')
    if posição % 2 == 1:
        print(f'R${tupla[posição]:>10.2f}')
    

print(f'{Fore.GREEN}{linha}{Fore.RESET}')
