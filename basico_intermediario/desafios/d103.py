def leiaInt(msg):
    from colorama import Fore
    print('=-' * 20)
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{Fore.RED}Digite um número inteiro válido!{Fore.RESET}')
            continue
        except (KeyboardInterrupt):
            print(f'{Fore.RED}O usuário preferiu não informar um valor!{Fore.RESET}')
            return 0
        else:
            return n

def leiaReal(msg):
    from colorama import Fore
    print('=-' * 20)
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print(f'{Fore.RED}ERRO: Digite um número real válido!{Fore.RESET}')
            continue
        except (KeyboardInterrupt):
            print(f'{Fore.RED}O usuário preferiu não informar um valor!{Fore.RESET}')
            return 0
        else:
            return n

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaReal('Digite um número real: ')

print(f'Você digitou {inteiro} como número inteiro')
print(f'Você digitou {real} como número real')