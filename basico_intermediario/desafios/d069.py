from colorama import Fore

brasileirão2012 = ('Fluminense', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Vasco da Gama', 'Corinthians', 'Botafogo', 'Santos', 'Cruzeiro', 
'Internacional', 'Flamengo', 'Náutico', 'Coritiba', 'Ponte Preta', 'Bahia', 'Portuguesa', 'Sport', 'Palmeiras', 'Atlético-GO', 'Figueirense')

print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')
print(f'A classificação dos times do Brasileirão 2012 foi: {Fore.GREEN}{brasileirão2012}{Fore.RESET}')
print(f'-=' * 15)
print(f'Os primeiros 5 colocados do {Fore.CYAN}Brasileirão 2012{Fore.RESET} foram: {Fore.GREEN}{brasileirão2012[0:5]}{Fore.RESET}')
print(f'-=' * 15)
print(f'Os quatro times {Fore.RED}REBAIXADOS{Fore.RESET} foram: {Fore.RED}{brasileirão2012[16:]}{Fore.RESET}')
print(f'-=' * 15)
print(f'Os times em ordem alfabética ficam: {Fore.GREEN}{sorted(brasileirão2012)}{Fore.RESET}')
print(f'-=' * 15)
posição = brasileirão2012.index('Náutico') + 1
print(f'O clube {Fore.RED}Clube Náutico Capibaribe{Fore.RESET} ficou na posição {Fore.GREEN}{posição}°{Fore.RESET}.')
print(f'{Fore.GREEN}-=' * 15, end='')
print(f'{Fore.RESET}')