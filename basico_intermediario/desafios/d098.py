def ficha(jogador = '', gols = 0):
    if jogador == '':
        jogador = '<desconhecido>'
    if str.isnumeric(gol) == False:
        gols = '0'
    else:
        gols = int(gols)
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato!')

nome = str(input('Qual o nome do jogador: ')).strip().capitalize()
gol = str(input('Quantos gols ele fez no campeonato: ')).strip()
ficha(nome, gol)