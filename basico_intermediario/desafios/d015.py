#Sorteio entre 4 alunos dee quem irá apagar o quadro
from random import choice

print('informe quais são os quatro alunos que serão sorteados: ')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
print(f'O aluno escolhido para apagar o quadro foi {choice([a1, a2, a3, a4])}.\n') #função que escolhe uma string aleatória
