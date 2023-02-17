from colorama import Fore

lista = []  #lista original
pares = []
ímpares = []
cont = 1

while True:
    print('=-' * 20)
    continuar = ' '
    lista.append(int(input(f'Digite o valor {Fore.RED}{cont}{Fore.RESET}: ')))
    while continuar != 'S' and continuar != 'N':
        continuar = input(f'Deseja Continuar {Fore.RED}[S | N]{Fore.RESET}: ').strip().upper()[0]
    if continuar == 'N':
        break
    cont += 1

for valores in lista:      
    if valores % 2 == 0:
        pares.append(valores)
    else:
        ímpares.append(valores)

print('=-' * 20)
print(f'A lista original é: {lista}')
print(f'A lista com apenas valores pares é: {pares}')
print(f'A lista apenas com valores ímpares é: {ímpares}')
