#Algorítimo que recebe um número e converte para binário, ou octal ou hexadecimal de acordo com a escolha do usuário?
from colorama import Fore

print(f'{Fore.MAGENTA}---------------------------------------------------------------------------------------------------------------------------------{Fore.RESET}')
escolha = int(input(f'Você quer converter o número para qual base? Digite {Fore.RED}(1){Fore.RESET} para Binário, {Fore.GREEN}(2){Fore.RESET} para Octal ou {Fore.BLUE}(3){Fore.RESET} para Hexadecimal: '))

if escolha != 1 and escolha !=2 and escolha != 3:
    print(f'Conversão Não Encontrada. Digite novamente entre os números {Fore.RED}(1){Fore.RESET}, {Fore.GREEN}(2){Fore.RESET}, ou {Fore.BLUE}(3)!{Fore.RESET}')
elif escolha == 1:
    numero = int(input(f'Você escolheu a conversão {Fore.RED}BINÁRIO{Fore.RESET}. Digite o número desejado para ser convertido: '))
    binario = bin(numero)[2:]
    print(f'O número {Fore.RED}{numero}{Fore.RESET} convertido para {Fore.RED}BINÁRIO{Fore.RESET} será {Fore.RED}{binario}{Fore.RESET}!!')
elif escolha == 2:
    numero = int(input(f'Você escolheu a conversão {Fore.GREEN}OCTAL{Fore.RESET}. Digite o número desejado para ser convertido: '))
    octal = oct(numero)[2:]
    print(f'O número {Fore.GREEN}{numero}{Fore.RESET} convertido para {Fore.GREEN}OCTAL{Fore.RESET} será {Fore.GREEN}{octal}{Fore.RESET}!!')
else:
    numero = int(input(f'Você escolheu a conversão {Fore.BLUE}HEXADECIMAL{Fore.RESET}. Digite o número desejado para ser convertido: '))
    hexadecimal = hex(numero)[2:]
    print(f'O número {Fore.BLUE}{numero}{Fore.RESET} convertido para {Fore.BLUE}HEXADECIMAL{Fore.RESET} será {Fore.BLUE}{hexadecimal}{Fore.RESET}!!')
print(f'{Fore.MAGENTA}---------------------------------------------------------------------------------------------------------------------------------{Fore.RESET}')