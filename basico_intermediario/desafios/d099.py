from colorama import Fore
def leiaint(msg):
    print(f'{msg}', end='')
    msg = str(input()).strip()
    while True:
        if str.isnumeric(msg) == True:
            msg = int(msg)
            return msg
        print(f'{Fore.RED}Digite um número inteiro válido!{Fore.RESET}')
        msg = str(input('Digite um número: ')).strip()

n = leiaint('Digite um número: ')
print(f'Você digitou o número {Fore.GREEN}{n}{Fore.RESET}.')
