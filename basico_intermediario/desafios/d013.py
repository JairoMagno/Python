#Programa que lê os catetos de um triângulo adjacente e retorna sua hipotenusa
import math

cato = float(input('Informe o valor do Cateto Oposto: '))
cata = float(input('Informe o valor do Cateto Adjacente: '))
hipo = math.hypot(cato, cata)  #função que calcula a hipotenusa de um triangulo retangulo
print(f'A hipotenusa dos catetos informados é de: {hipo:.2f}')