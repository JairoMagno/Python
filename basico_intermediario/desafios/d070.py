from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('A tupla gerada de forma aleatória foi: ', end='')
for c in tupla:
    print(f'{c} ', end='')
print(f'\nO maior valor foi {max(tupla)}') #função que retorna o maior valor dentro da tupla
print(f'O menor valor foi {min(tupla)}') #Função que retorna o menor valor dentro da tupla