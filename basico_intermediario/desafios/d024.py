#Algorítimo em que o computador escolhe um valor de 0 a 5 e pede pro usuário adivinhar. Caso acerte, mensagem "acertou", caso erre, mensagem "errou:":

from random import randint

numero = int(input('Informe um valor de 0 até 5: '))
pc = randint(0,5)
if numero == pc:
    print(f'Parabéns, você adivinhou o número do computador ({pc}).')
else:
    print(f'Sinto muito, o número escolhido pelo computador foi {pc}')
print('---FIM---')


