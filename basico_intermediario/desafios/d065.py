#Programa que lê o nome, idade e sexo de n pessoas e informa a média do grupo, Qual o homem mais velho e quantas mulheres tem menos de 21:

from colorama import Fore

print('Digite as seguintes informações abaixo para n pessoas:')
maioridade = homem = mulher = 0
cont = 1

while True: 
    print(f'{Fore.GREEN}-=' * 15, end='')
    print(f'{Fore.RESET}')

    idade = int(input(f'Qual a idade da pessoa {cont}: '))
    cont += 1
    sexo = input(f'Qual é seu sexo {Fore.GREEN}[M | F]:{Fore.RESET} ').strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite novamente.{Fore.RESET}')
        sexo = input(f'Qual é seu sexo {Fore.GREEN}[M | F]:{Fore.RESET} ').strip().upper()[0]
    saida = input('Deseja continuar informando dados [S | N]? ').strip().upper()[0]
    while saida != 'S' and saida != 'N':
        print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite novamente.{Fore.RESET}')
        saida = input('Deseja continuar informando dados [S | N]? ').strip().upper()[0]

    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if idade > 18:
        maioridade += 1
    if saida == 'N':
        break

print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')

if maioridade == 0:
    print('Não houve ninguém no grupo com mais de 18 anos!!')
elif maioridade == 1:
    print(f'Apenas {Fore.GREEN}1{Fore.RESET} pessoa tinha mais de 18 anos!!')
else:
    print(f'{Fore.GREEN}{maioridade}{Fore.RESET} pessoas tinham mais de 18 anos!!')

if homem == 0:
    print('Não houve homens no grupo para serem cadastrado!!')
elif homem == 1:
    print(f'Apenas {Fore.GREEN}1{Fore.RESET} homem foi cadastrado!!')
else:
    print(f'{Fore.GREEN}{homem}{Fore.RESET} homens foram cadastrados!!')

if mulher == 0:
    print('Nenhuma mulher com menos de 20 anos!')
else:
    if mulher >= 2:
        print(f'{Fore.RED}{mulher}{Fore.RESET} mulheres possuem menos de {Fore.RED}20{Fore.RESET} anos!!')
    else:
        print(f'Apenas {Fore.RED}{mulher}{Fore.RESET} mulher possue menos de {Fore.RED}20{Fore.RESET} anos!!')
        