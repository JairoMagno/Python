#Algorítimo que pergunta a distância de uma viagem em km e informa o valor da passagem.
#Se a distância for menor ou igual a 200km, será cobrado R$0,50 por cada km rodado.
#Se a distância for maior que 200km, será cobrado R$0,45 por cada km rodado.

from math import floor

distancia = float(input('Qual será a distância de sua viagem em km? '))
if distancia <= 200:
    valor = floor(distancia) * 0.5
    print(f'O valor cobrado para uma viagem de {distancia}km será R${valor:.2f}.')
else:
    valor = floor(distancia) * 0.45
    print(f'O valor cobrado para uma viagem de {distancia}km será R${valor:.2f}.')
print('---FIM---')