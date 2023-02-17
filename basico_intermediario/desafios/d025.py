#Algorítimo que checa se um carro estava acima de 80km/h. A cada km acima do limite, será acrescido R$7,00 reais na multa
#Ex: 85km/h = 7*(85-80) = R$35,00.

from math import floor

velocidade = float(input('Informa a velocidade do carro: '))
if velocidade <= 80:
    print('Tudo ok! Sua velocidade está dentro dos limites permitidos.')
else:
    multa = 7*(floor(velocidade) - 80)
    print(f'VOCÊ ESTÁ ACIMA DA VELOCIDADE PERMITIDA. Será aplicado uma multa de R${multa}')
print('---FIM---')
