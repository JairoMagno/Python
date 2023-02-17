#Algorítimo que lê um número e retorna sua parte inteira
import math

num = float(input('Digite um numero real: '))
mod = math.trunc(num) #Função que retorna sua parte inteira
print(f'A parte inteira do número {num} será: {mod}.') 