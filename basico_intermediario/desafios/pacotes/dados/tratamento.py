def leiadinheiro(msg):
    from colorama import Fore
    print('=-' * 20)
    print(msg, end='')
    msg = str(input('')).strip()
    while True:
        if msg.replace(',','').isdigit() == True:
            msg = msg.replace(',','.')
            msg = float(msg)
            return msg
        elif msg.replace('.','').isdigit() == True:
            msg = float(msg)
            return msg
        else:
            print(f'{Fore.RED}ERRO: \"{msg}\" não é um número!{Fore.RESET}')
            msg = str(input('Digite o preço: R$'))


def menu(msg):
    print('=' * 40)
    print(f'{msg}'.center(40))
    print('=' * 40)

