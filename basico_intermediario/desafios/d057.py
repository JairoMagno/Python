#Algorítimo que calcula uma PA usando while:

from colorama import Fore

n1 = int(input('Digite o primeiro termo da PA: '))
termos = int(input('Quantos termos terá a PA: '))
razao = int(input('Qual a razão dessa PA: '))
contagem = 0
pa = n1

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
while contagem < termos:

    print(f'{Fore.GREEN}{pa} ⇀ ', end='')
    pa += razao
    contagem += 1

print(f' FIM{Fore.RESET}')
print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
somatermos = termos * (n1 + (pa)) / 2
print(f'A soma da PA de {termos} termos com razão {razao} é: {somatermos:.2f}')