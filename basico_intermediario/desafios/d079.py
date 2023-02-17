cont = 0

expressão = input('Digite sua expressão matemática: ')
lista = []
for parenteses in expressão:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
        
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
    print(lista)
