#Programa que gera uma matrix 3x3
from colorama import Fore

matrix1 = [[0,0,0],[0,0,0],[0,0,0]]
somapar = soma3 = maior2 = 0

print('=-' * 30)
for linha in range (0, 3):
    for coluna in range(0, 3):
        matrix1[linha][coluna] = int(input(f'Digite um valor para {Fore.GREEN}[{linha}, {coluna}]{Fore.RESET}: '))

        if matrix1[linha][coluna] % 2 == 0:   #Soma de todos os valores pares
            somapar += matrix1[linha][coluna]

        if coluna == 2:                       #Soma de todos os valores da coluna 3 
            soma3 += matrix1[linha][2]

maior2 = max(matrix1[1])                      #Verificando quem é o maior valor da linha 1
print('=-' * 30)
print(f'A lista que contém as 3 listas fica da seguinte forma: {Fore.GREEN}{matrix1}{Fore.RESET}')
print('A lista em forma matricial fica da seguinte forma: ')

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{Fore.GREEN}[{matrix1[linha][coluna]:^5}]', end=' ')
    print()
print(f'{Fore.RESET}=-' * 30)

print(f'A soma de todas os valores pares é: {somapar}')
print(f'A soma de todos os valores da coluna 3 é: {soma3}')
print(f'O maior valor da segunda linha é: {maior2}')
