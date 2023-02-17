"""Programa que lê a largura e altura de uma parede. A partir disso calcula sua área e quantidade de tinta 
necessária pra pintar a parade. Cada litro de tinta pinta 2m²"""

l = float(input('Informa a largura da parede em metros: '))
a = float(input('informa a altura da parede em metros:'))
print(f'A área da parede será de {l*a}m² e a quantidade de tinta necessária para pintar é de {(l*a)/2}l.\n')