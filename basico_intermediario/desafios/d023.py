#Programa que lê um nome completo e informa o seu primeiro e último nome separadamente:

nome = input('informa seu nome completo: ').strip()
n1 = nome.split()
n2 = n1[-1]
print(f'Primeiro nome: {n1[0].capitalize()}')
print(f'Último nome: {n2.capitalize()}')