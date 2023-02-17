from random import randint
from time import sleep
from operator import itemgetter

dados = {'Jogador 1': randint(1,6),
         'jogador 2': randint(1,6),
         'jogador 3': randint(1,6),
         'jogador 4': randint(1,6)}
print(dados)
ranking = list()
print('=-' * 30)
for keys, values in dados.items():
    print(f'- O {keys} tirou: {values}')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'O {v[0]} ficou em {i+1}° Lugar, tirando {v[1]}')
    