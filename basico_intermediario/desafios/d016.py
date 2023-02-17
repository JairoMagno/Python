#Sorteio entre 4 alunos de qual será a ordem entre eles para uma apresentação:
from random import shuffle

print('informe quais são os quatro alunos que serão sorteados a ordem: ')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
ordem = [a1, a2, a3, a4]
shuffle(ordem)  #função que escolhe uma string aleatória
print(f'A ordem de apresentação entre os alunos será: {ordem}.\n') 