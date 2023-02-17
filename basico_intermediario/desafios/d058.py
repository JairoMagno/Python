#Algorítimo V2.0 do cálculo de um PA do exercício 57:

from colorama import Fore

n1 = int(input(f'Digite o {Fore.GREEN}PRIMEIRO{Fore.RESET} termo da PA: '))
termos = int(input(f'Quantos {Fore.GREEN}TERMOS{Fore.RESET} terá a PA: '))
razao = int(input(f'Qual a {Fore.GREEN}RAZÃO{Fore.RESET} dessa PA: '))
contagem = 0
pa = n1
opção = -1
soma = 0
termos1 = 0
somatermos = 0

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')

while contagem < termos:

    print(f'{Fore.GREEN}{pa} ⇀ ', end='')
    pa += razao
    soma += pa - razao
    contagem += 1
print(f' PAUSA{Fore.RESET}')

contagem = 0

while opção != 0:
    print(f'{Fore.MAGENTA}-=' * 20)
    print(f'{Fore.RESET}', end='')
    print(f"""Você deseja adicionar mais uma quantidade de termos para essa PA
    Digite {Fore.GREEN}[ 0 ]{Fore.RESET} para encerrar a contagem
    Digite {Fore.GREEN}[ 1 ]{Fore.RESET} para adicionar termos""")
    opção = int(input('Qual a sua opção? '))

    if opção != 0 and opção != 1:
        print(f'{Fore.RED}Opção inválida!!!{Fore.RESET} escolha uma das seguintes opções: ')

    if opção == 1:
        termos1 = int(input('Quantos termos você deseja adicionar a PA: '))
        print(f'{Fore.MAGENTA}-=' * 20)
        print(f'{Fore.RESET}', end='')

        while contagem < termos1:
            print(f'{Fore.GREEN}{pa} ⇀ ', end='')
            pa += razao
            soma += pa - razao
            somatermos += 1
            contagem += 1
        print(f' FIM{Fore.RESET}')
    contagem = 0

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
termos += somatermos
print(f'A soma da PA de {Fore.GREEN}{termos}{Fore.RESET} termos com razão {Fore.GREEN}{razao}{Fore.RESET} é: {Fore.GREEN}{soma:.2f}{Fore.RESET}')
