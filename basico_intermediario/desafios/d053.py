#Algorítimo que verifica sexo de uma pessoa e repete caso a reposta seja inválida:

from colorama import Fore

contagem = 1
condição = ''
homens = 0
mulheres = 0

while condição != 'N':
    print(f'{Fore.MAGENTA}-=' * 10, end='')
    print(f'{Fore.RESET}')

    sexo = input(f'Qual sexo da pessoa {contagem}, [M | F]: ').strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = input('Resposta inválida. Digite entre [M | F]: ').strip().upper()[0]
    contagem += 1

    if sexo == 'M':
        homens += 1

    if sexo =='F':
        mulheres +=1

    condição = input('Você deseja continuar? [S | N]: ').strip().upper()[0]
    while condição != 'S' and condição != 'N':
        condição = input('Resposta inválida. Digite entre [S | N]: ').strip().upper()[0]

print(f'{Fore.MAGENTA}-=' * 10)
print(f'{Fore.RESET}', end='')

if homens == 1 and mulheres == 0:
    print('Apenas 1 Homem participou dessa pesquisa!')
elif homens == 0 and mulheres == 1:
    print('Apenas 1 Mulher participou dessa pesquisa!')
elif homens == 1 and mulheres ==1:
    print('Apenas 1 Homem e 1 Mulher participaram dessa pesquisas')
else:
    print(f'{contagem - 1} pessoas participaram da pesquisa. {homens} pessoas dos pesquisados eram homens e {mulheres} eram mulheres!')