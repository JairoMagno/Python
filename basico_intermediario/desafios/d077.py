from colorama import Fore

lista = []  #lista original
cont = 1
continuar = ' '
while True:
    print('=-' * 20)
    lista.append(int(input(f'Digite o valor {Fore.RED}{cont}{Fore.RESET}: ')))

    while continuar != 'S' and continuar != 'N':
        continuar = input(f'Deseja Continuar {Fore.RED}[S | N]{Fore.RESET}: ').strip().upper()[0]
    if continuar == 'N':
        break
    cont += 1
    continuar = ' '


print('=-' * 20)
lista.sort(reverse=True)
print(f'{len(lista)} números foram digitados')
print(f'Os valores apresentados na lista em ordem decrescente: {lista}')
print(f'A posição do número 5 é: ', end='')
if 5 in lista:
    for posição, valor5 in enumerate(lista):
        if valor5 == 5:
            print(f'{posição + 1}°...', end='')
else:
    print('Nenhuma, pois o valor não foi digitado')