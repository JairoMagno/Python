#Algorítimo que lê o primeiro termo e a razão de uma PA. No final mostra os 10 primeiros termos dessa progressão

from colorama import Fore

t1 = int(input('Qual será o primeiro termo da sua PA: '))
razao = int(input('Qual será a razão dessa PA: '))
enésimo = t1 + (10 - 1) * razao #Fórmula do n-ésimo termo de uma pa
print(f'{Fore.GREEN}-=' * 10)
cont = 0

for c in range(t1, enésimo + razao, razao):
    cont += 1
    print(f'Termo {cont} = {c}')

print('-=' * 10, end='')
print(f'{Fore.RESET}')