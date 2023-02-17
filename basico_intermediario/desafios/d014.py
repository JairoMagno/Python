#Algorítimo que lê um ângulo em graus:
from math import sin, cos, tan, radians
#radians converte um valor em graus e converte para radianos.
ang = float(input('Digite um valor de ângulo do círculo trigonométrico em graus: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O seno do ângulo {ang}° é de {seno:.2f}.')
print(f'O cosseno do ângulo {ang}° é de {cosseno:.2f}.')
print(f'A tangente do ângulo {ang}° é de {tangente:.2f}.')