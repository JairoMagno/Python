#Algorítimo de um menu que lê dois números e apresenta algumas possibilidades:

from colorama import Fore

print('Apresente abaixo dois números desejados: ')
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
escolha = 0

while escolha != 5:
    print(f'{Fore.MAGENTA}-=' * 20)
    print(f'{Fore.RESET}', end='')
    print(f"""    Digite {Fore.GREEN}[ 1 ]{Fore.RESET} para somar
    Digite {Fore.GREEN}[ 2 ]{Fore.RESET} para multiplicar
    Digite {Fore.GREEN}[ 3 ]{Fore.RESET} para verificar qual número é maior
    Digite {Fore.GREEN}[ 4 ]{Fore.RESET} para verificar novos números
    Digite {Fore.GREEN}[ 5 ]{Fore.RESET} para sair do programa""")
    escolha = int(input('Escolha uma opção: '))

    if escolha > 5:
        print('Escolha inválida!!! Digite uma das opção apresentadas: ')
    elif escolha < 1:
        print('Escolha inválida!!! Digite uma das opção apresentadas: ')

    if escolha == 1:
        print(f'A soma entre os números selecionados será: {Fore.GREEN}{n1} + {n2} = {n1 + n2}!{Fore.RESET}')

    if escolha == 2:
        print(f'A multiplicação entre os números selecionados será? {Fore.GREEN}{n1} X {n2} = {n1 * n2}!{Fore.RESET}')

    if escolha == 3:
        if n1 > n2:
            print(f'O número {Fore.GREEN}{n1}{Fore.RESET} é maior que {Fore.GREEN}{n2}{Fore.RESET}!')
        elif n2 > n1:
            print(f'O número {Fore.GREEN}{n2}{Fore.RESET} é maior que {Fore.GREEN}{n1}{Fore.RESET}!')
        else:
            print(f'Os números {Fore.GREEN}{n1}{Fore.RESET} e {Fore.GREEN}{n2}{Fore.RESET} são iguais!')

    if escolha == 4:
        print('Quais serão os números novos?')
        n1 = int(input('Digite o número 1: '))
        n2 = int(input('Digite o número 2: '))

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print('Obrigado por participar desse menu :)')
