#Algorítimo para o aluguel de um carro. O carro custa R$60 por dia e R$0,15 por Km rodado. Calcule o preço a pagar

dias = int(input('Quantos dias o cliente ficou com o carro: '))
km = float(input('Quantos Km o carro do cliente rodou: '))
total = (60 * dias) + (0.15 * km)
print(f'O total que o cliente precisa pagar por ter ficado {dias} dias com o carro e rodado {km}Km, será de R${total:.2f}.\n')
