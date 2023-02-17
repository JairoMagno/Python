lista = [[],[]]
for c in range(0, 7):
    numero = int(input(f'Digite o número {c + 1}: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    if numero % 2 == 1:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'A lista dos números pares é: {lista[0]}')
print(f'A lista dos números ímpares é: {lista[1]}')
