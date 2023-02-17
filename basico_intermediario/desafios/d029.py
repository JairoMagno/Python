#informe entre 3 números qual é o maior e qual o menor

print('---COMEÇO---')
print('Escolha 3 valores para checar qual é o maior e menor entre eles:')
n1 = float(input('Informe o valor 1: '))
n2 = float(input('Informe o valor 2: '))
n3 = float(input('Informe o valor 3: '))
#Checagem do maior valor
if (n1 >= n2 and n1 >= n2) == True:
    print(f'O número {n1} é o maior número')
elif (n2 >= n1 and n2 >= n3) == True:
    print(f'O número {n2} é o maior número')
else:
    print(f'O número {n3} é o maior valor')
#Checagem do menor valor
if (n1 <= n2 and n1 <= n2) == True:
    print(f'O número {n1} é o menor número')
elif (n2 <= n1 and n2 <= n3) == True:
    print(f'O número {n2} é o menor número')
elif (n3 <= n1 and n3 <= n3) == True:
    print(f'O número {n3} é o menor valor')
print('---FIM---')