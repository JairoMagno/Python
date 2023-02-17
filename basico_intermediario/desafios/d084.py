lista = []
while True:
    print('=-' * 30)
    continuar = ''
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    lista.append([nome, [nota1, nota2], media]) #juntando todos os valores dentro de uma lista com listas
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print('=-' * 30)
print('No.  Nome        Média')
print('=-' * 30)
for posição, valor in enumerate(lista):
    print(f'{posição}    {lista[posição][0]:^6}       {lista[posição][2]:>4.2f}')

while True:
    print('=-' * 30)
    mostrar = int(input('Mostrar as notas de qual aluno [999 interrompe]: ')) 
    if mostrar == 999:
        break
    print(f'AS nota de {lista[mostrar][0]} são: {lista[mostrar][1]}.')
print('=-' * 30)