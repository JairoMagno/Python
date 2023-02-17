#Programa que cria uma tupla totalmente preenchida com uma contagem por extenso , de zero até vinte
#O algorítimo deve ler um número do teclado (entre 0 e vinte) e mostrá-lo por extenso

from colorama import Fore

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Qual número de 0 até 20 você deseja ver por extenso: '))
    if numero < 0 or numero > 20:
        print('INFORMAÇÃO INVÁLIDA. Digite novamente.')
    if numero >= 0 and numero <= 20:
        break
print(f'O número {Fore.GREEN}{numero}{Fore.RESET} em extenso é {Fore.GREEN}{contagem[numero]}{Fore.RESET}')