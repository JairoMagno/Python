#Aproveitamento de um atacante:

dados = dict()
lista = list()
cont = jogador = 0

while True:
    print('=-' * 30)
    dados.clear()
    continuar = ''
    listaGols = list()
    dados['Nome'] = str(input('Qual o nome do atacante: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

    for c in range (0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}: '))
        listaGols.append(gols)
    dados['Gols'] = listaGols[:]
    dados['Total'] = sum(listaGols)
    lista.append(dados.copy())

    while True:
        continuar = str(input('Deseja continuar informando [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Informação inválida. Digite Novamente')
    if continuar == 'N':
        break

print('=-' * 30)
print(lista)
print('=' * 50)
print('Cod Nome           Gols           Total')
for i, v in enumerate(lista):
    print(f'{i:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print('=-' * 30)
    cont = 0
    jogador = int(input('Mostrar dado de qual jogador [999 interrompe]: '))
    if jogador == 999:
        break
    if jogador >= len(lista):
        print('Jogador não encontrado. Digite novamente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[jogador]["Nome"]} --')
        for i, v in enumerate(lista[jogador]["Gols"]): #acessando a lista de gols dentro de um dicionário, dentro de uma lista
            print(f' => No jogo {i}, fez {v} Gols!')
print('=-' * 30)
