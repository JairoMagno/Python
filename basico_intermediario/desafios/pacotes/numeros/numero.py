def formatar(preço):
    x = str(preço)
    y = x.replace('.',',')
    return y


def valor(preço, format=False):
    if format == True:
        return formatar(preço)
    else:
        return preço 


def metade(preço, format=False):
    p = f'{preço / 2:.2f}'
    if format == True:
        return formatar(p)
    else:
        return p


def dobro(preço, format=False):
    p = f'{preço * 2:.2f}'
    if format == True:
        return formatar(p)
    else:
        return p


def aumentar(preço, x,format=False):
    p = f'{preço * ((x+100)/100):.2f}'
    if format == True:
        return formatar(p)
    else:
        return p


def reduzir(preço, y,format=False):
    p = f'{preço * ((100-y)/100):.2f}'
    if format == True:
        return formatar(p)
    else:
        return p


def resumo(preço, x, y):
    from colorama import Fore
    msg = 'RESUMO DOS VALORES PEDIDOS'
    tam = len(msg) + 6
    print(f'{Fore.GREEN}=' * tam)
    print(f'   {msg}')
    print('=' * tam)
    print(f'{Fore.RESET}{"Preço analizado:":<3}    R${valor(preço, True):<15}')
    print(f'{"Dobro do preço:":<3}     R${dobro(preço, True):<15}')
    print(f'{"Metade do preço:":<3}    R${metade(preço, True):<15}')
    print(f'{f"{x}% de aumento:":<3}     R${aumentar(preço, x,True):<15}')
    print(f'{f"{y}% de redução:":<3}     R${reduzir(preço, y,True):<15}')
    print('=' * tam)


def leiaInt(msg):
    from colorama import Fore
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{Fore.RED}Digite um número inteiro válido!{Fore.RESET}')
            continue
        except (KeyboardInterrupt):
            print(f'{Fore.RED}O usuário preferiu não informar um valor! Programa será encerrado...{Fore.RESET}')
            return 3
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