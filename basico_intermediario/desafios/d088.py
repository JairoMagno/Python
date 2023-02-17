#Aproveitamento de um atacante:

dados = dict()
listaGols = list()
cont = 0

dados['Nome'] = str(input('Qual o nome do atacante: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

for c in range (0, partidas):
    gols = int(input(f'Quantos gols na partida {c+1}: '))
    listaGols.append(gols)
dados['Gols'] = listaGols[:]
dados['Total'] = sum(listaGols)

print('=-' * 30)
print(dados)
print('=-' * 30)

for keys, values in dados.items():
    print(f'O campo {keys} tem o valor {values}.')
print('=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas:')
for c in listaGols:
    print(f' => Na partida {cont+1}, fez {c} gols')
    cont += 1
print(f'Foi um total de {sum(listaGols)} gols!')