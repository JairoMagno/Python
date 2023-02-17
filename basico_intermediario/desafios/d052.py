#Programa que lê o nome, idade e sexo de 4 pessoas e informa a média do grupo, Qual o homem mais velho e quantas mulheres tem menos de 21:

from colorama import Fore

print('Digite as seguintes informações abaixo para 4 pessoas:')
soma = 0
homem = 0
mulher = 0
nomeh = ''

for c in range(1, 5):
    print(f'{Fore.GREEN}-=' * 15, end='')
    print(f'{Fore.RESET}')

    nome = input(f'Qual o nome da pessoa {c}: ').strip().upper()
    idade = int(input(f'Qual a sua idade: '))
    soma += idade
    sexo = input('Qual é seu sexo [M | F]: ').strip().upper()

    if sexo == 'M' and idade > homem:
        nomeh = nome
        homem = idade
    if sexo == 'F' and idade < 20:
        mulher += 1

    print(f'{Fore.GREEN}-=' * 15, end='')
    print(f'{Fore.RESET}')

media = soma / c
print(f'A média de grupo é de {Fore.RED}{media:.2f}{Fore.RESET} anos!')

if homem == 0:
    print('Não houve homens no grupo para ser calculado qual o mais velho!!')
else:
    print(f'{Fore.RED}{nomeh}{Fore.RESET} é o homem mais velho com {Fore.RED}{homem}{Fore.RESET} anos')

if mulher == 0:
    print('Nenhuma mulher com menos de 20 anos!')
else:
    if mulher >= 2:
        print(f'{Fore.RED}{mulher}{Fore.RESET} mulheres possuem menos de {Fore.RED}20{Fore.RESET} anos!!')
    else:
        print(f'{Fore.RED}{mulher}{Fore.RESET} mulher possue menos de {Fore.RED}20{Fore.RESET} anos!!')
        