from colorama import Fore

lista = []  #lista original
cont = 1
continuar = ' '
while True:

    valor = int(input(f'Qual o valor do {Fore.GREEN}número {cont}{Fore.RESET}: '))

    if valor not in lista:   
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, portanto não será adicionado...')

    while continuar != 'S' and continuar != 'N':
        continuar = input(f'Deseja Continuar {Fore.RED}[S | N]{Fore.RESET}: ').strip().upper()[0]
    if continuar in 'N':
        break
    cont += 1
    continuar = ''

lista.sort()
print('=-' * 20)
print(f'Os valores apresentados na lista em ordem númerica sem duplicatas são: {lista}')