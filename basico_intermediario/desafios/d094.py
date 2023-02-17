from time import sleep
def maiorNumero(* num):
    print('=-' * 30)
    maior = 0
    cont = 0
    print('Analisando os valores passados...')
    for c in sorted(num):
        if cont == 0 or c > maior:
            maior = c 
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
        cont += 1
    print(f'. Foram informados {len(num)} valores ao todo!')
    print(f'O maior número da lista informada é {maior}')
    sleep(2)

maiorNumero(8, 9, 100, 8, 6)
maiorNumero(10, 11, 12, 20)
maiorNumero(500, 200, 1000, 5000)
maiorNumero()
