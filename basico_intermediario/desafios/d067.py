#Algorítimo que simula um caixa Eletrônico:

from colorama import Fore

linha = '=' * 50
titulo = 'BANCOS MAGNO & RODRIGUES'
print(f'{Fore.GREEN}{linha}')
print(titulo.center(50))
print(f'{linha}{Fore.RESET}')
valorsaque = int(input('Qual será o valor sacado: R$'))
total = valorsaque
cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        else:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break

print(f'{Fore.GREEN}{linha}{Fore.RESET}')
print(f'Volte sempre ao {Fore.GREEN}BANCOS MAGNO & RODRIGUES!{Fore.RESET} Tenha um ótimo dia.')




#Outra forma feita sem utilizar estruturas de repetição!! 
"""cedula50 = valorsaque // 50
#if valorsaque % cedula50 == 0:
print(f'Total de {cedula50} cédulas de R$50')
cedula20 = (valorsaque - (cedula50 * 50)) // 20
print(f'Total de {cedula20} cédulas de R$20')
cedula10 = (valorsaque - (cedula50 * 50) - (cedula20 * 20)) // 10
print(f'Total de {cedula10} cédulas de R$10')
cedula1 = (valorsaque - (cedula50 * 50) - (cedula20 * 20) - (cedula10 * 10))
print(f'Total de {cedula1} cédulas de R$1')"""