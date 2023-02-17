#Algorítimo que calcula a quantidade de número primos dentro de um determinado intervalo:

from colorama import Fore

intervalo = int(input('Até qual intervalo será verificado quantos números primos existem: '))
print(f'{Fore.GREEN}-=' * 10)
cont = 0
soma = 0
primo = 0

if intervalo <= 1:
    print('Números Negativos, nulos ou igual a 1 NÃO são primos!')
elif intervalo > 1:
    for c in range (2, intervalo + 1):
        if ((c % 2 != 0) and (c % 3 != 0) and (c % 5 != 0) and (c % 7 !=0)) or (c == 2) or (c == 3) or (c == 5) or (c == 7):
            print(f'{c}', end=' ')
            cont += 1
            soma += c

print('\n', end='')
print('-=' * 10, end='')
print(f'{Fore.RESET}')
print(f'No intervalo até {intervalo}, existem {cont} números primos e sua soma total é de {soma}.')

'''for i in range(1, intervalo + 1):
        if c % i == 0:
            primo += 1
    if primo == 2:
        print(c)
    if primo == 2:
        print(f'{c}', end=' ')
        soma += c
        cont += 1'''