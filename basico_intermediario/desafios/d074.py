lista = []

for c in range(1, 6):
    lista.append(int(input(f'Digite o valor {c} da lista: ')))

print('=-' * 20)
print(f'A lista criada tem os seguintes valores: {lista}')
print(f'O maior valor da lista é o {max(lista)}, na posição ', end='')

for posição, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posição}...', end='')

print(f'\nO menor valor da lista é o {min(lista)}, na posição ', end='')

for posição, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posição}...', end='')
        