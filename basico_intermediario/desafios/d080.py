lista1 = []
lista2 = []
maior = menor = 0
while True:
    continuar = ''
    print('=-' * 30)
    lista1.append(str(input('Qual o nome da pessoa: ')))
    lista1.append(float(input('Qual o peso da pessoa: ')))
    if len(lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor: 
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar cadastrando [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('=-' * 30)
print(f'- A lista com todas as pessoas e seus respectivos pesos foi: {lista2}')
print(f'- {len(lista2)} pessoas foram cadastradas!')

print(f'- A pessoa mais pesada teve {maior:.2f}Kg. Peso de ', end='')
for posição, peso in enumerate(lista2):
    if maior == lista2[posição][1]:
        print(f'"{lista2[posição][0]}" ', end='')

print(f'\n- A pessoa mais leve teve {menor:.2f}Kg. Peso de ', end='')
for posição, peso in enumerate(lista2):
    if menor == lista2[posição][1]:
        print(f'"{lista2[posição][0]}" ', end='')
