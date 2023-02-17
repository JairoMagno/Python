tupla = ('Jairo', 'Raquel', 'Carlos', 'Arthur', 'Gabriel', 'Mateus', 'Naruto', 'Pokemon')

for palavra in tupla:
    print(f'\nNa palavra "{palavra}", temos ', end='')
    for vogal in palavra:                             #Nested For! Varrer a tupla e dentro de cada palavra na tupla, varrer suas vogais.
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')

