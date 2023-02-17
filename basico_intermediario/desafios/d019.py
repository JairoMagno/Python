#Algorítimo que lê um número de 0 até 9999 e informa unidade, dezena, centena e milhar:

#Fazendo por manipulação de string
"""n = input('Informe um numéro de 0 até 9999: ')
ordem = '000' + n #concatenando strings
print(f'A sua unidade é: {ordem[-1]}') #Usando [-1] eu pego o valor de trás pra frente (ex: 9245. n[-1] = 5 e n[-4] = 9)
print(f'A sua dezena é: {ordem[-2]}')
print(f'A sua centena é: {ordem[-3]}')
print(f'O seu milhar é: {ordem[-4]}')"""

#Fazendo por manipulação matemática
n = int(input('Informe um numéro de 0 até 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'A sua unidade é: {u}') 
print(f'A sua dezena é: {d}')
print(f'A sua centena é: {c}')
print(f'O seu milhar é: {m}')



