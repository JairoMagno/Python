#Algorítimo que lê uma palavra/frase e verifica se ela é um palídromo:

from colorama import Fore

palavra = input('Digite uma palavra/frase para verificar se é um palíndromo: ').strip().upper()
#print(''.join(reversed(palavra.upper().strip())))

print(f'{Fore.GREEN}-=' * 10)

if palavra.replace(' ','') == ''.join(reversed(palavra.replace(' ',''))):
    print(f'A palavra/frase "{palavra.upper()}" É um palídromo')
else:
    print(f'A palavra/frase NÃO é um palídromo. Sua inversão fica: ', end='')
    print(''.join(reversed(palavra)))

print('-=' * 10, end='')
print(f'{Fore.RESET}')
