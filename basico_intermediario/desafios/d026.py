#Programa que informa se um número é par ou ímpar:

n = int(input('Informe um valor: '))
if ((n % 2) == 0):
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é ÍMPAR.')
print('---FIM---')