from colorama import Fore

tupla = (int(input('Digite o número 1: ')),
            int(input('Digite o número 2: ')),
                int(input('Digite o número 3: ')),
                    int(input('Digite o número 4: ')))

print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')

print(f'Você digitou os valores {tupla}')
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
if tupla.count(3) >= 1:
    print(f'A primeira vez que o número 3 foi digitado foi na posição {tupla.index(3) + 1}°')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
pares = 0
for c in tupla:
    if c % 2 == 0:
        print(f'{c}', end=' ')
        pares += 1
if pares == 0:
    print('Nenhum')
print('\n')
print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')
