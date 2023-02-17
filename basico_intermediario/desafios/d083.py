from random import randint
from time import sleep

jogo = []
megasena = []
cont = 0
título = 'MEGA SENA'
print('=' * 50)
print(f'{título.center(50)}')
print('=' * 50)

sorteios = int(input('Quantas vezes você quer fazer o sorteio da Mega Sena: '))
entrada = (f'  SORTEANDO {sorteios} JOGOS  ')
print(entrada.center(50, '='))

for c in range(1, sorteios + 1):
    sleep(1)
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
        if cont >= 6:
            break
        cont += 1
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    megasena.append(jogo[:])
    jogo.clear()
    cont = 0
saida = '  BOA SORTE  '
print(saida.center(50, '='))
print(f'Lista de todos os jogos: {megasena}')
print('=' * 50)