#Ordenando uma lista sem utilizar o sort()

lista = []
print('Digite os valores da sua lista: ')

for c in range(0, 5):
    numero = int(input(f'Qual o valor do número {c}: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Número adicionado ao final da lista!')
    else:
        posição = 0
        while posição < len(lista):
            if numero <= lista[posição]:
                lista.insert(posição, numero)
                print(f'Número adicionado na posição {posição}!')
                break
            posição += 1

print('=-' * 20)
print(f'A sua lista em ordem é: {lista}')