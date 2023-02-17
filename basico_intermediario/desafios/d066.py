#Algorítimo que lê o nome e preço de um produto. O programa deve perguntar se o usuário quer continuar.
#No final mostra qual o total gasto, quantos produtos foram mais de R$1000,00 e qual o nome do produto mais caro.

from colorama import Fore

caro = maisbarato = total = 0
cont = 1
nomebarato = ''

while True:
    print(f'{Fore.GREEN}-=' * 15, end='')
    print(f'{Fore.RESET}')

    nome = input(f'Qual o nome do produto {cont}: ').strip().upper()
    preço = float(input('Qual o preço desse produto: '))
    while preço < 0:
        print(f'{Fore.RED}OPÇÃO INVÁLIDA! Não existem produtos com preços negativos, digite novamente.{Fore.RESET}')
        preço = float(input('Qual o preço desse produto: '))
    total += preço
    saida = input('Deseja continuar informando dados [S | N]? ').strip().upper()[0]
    while saida != 'S' and saida != 'N':
        print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite novamente.{Fore.RESET}')
        saida = input('Deseja continuar informando dados [S | N]? ').strip().upper()[0]
    
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomebarato = nome   
    if preço > 1000:
        caro += 1
    cont += 1
    if saida == 'N':
        break

print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')
print(f'{Fore.GREEN}PROGRAMA FINALIZADO!!{Fore.RESET}')
print(f'O total gasto na compra foi {Fore.GREEN}R${total:.2f}{Fore.RESET}')
print(f'A quantidade de produtos que custam mais de {Fore.GREEN}R$1000,00{Fore.RESET} foi : {Fore.GREEN}{caro}{Fore.RESET}')
print(f'O produto mais barato foi {Fore.GREEN}{nomebarato}{Fore.RESET}, custando {Fore.GREEN}R${maisbarato:.2f}{Fore.RESET}')
