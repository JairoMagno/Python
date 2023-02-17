def fatorial(n, show=False):
    """Calculo fatorial de um número natural à escolha do usuário.

    Args:
        n (Tipo: Inteiro): Valor escolhido para calcular o seu fatorial.
        show (booleano, opcional): Valor opcional. Caso o usuário utilize True, mostrará na tela a conta do fatorial.

    Returns:
        Tipo(Inteiro): O valor fatorial do número n.
    """
    print('=-' * 20)
    if n < 0:
        return 'Valores negativos não possuem fatorial'
    else:
        i = 1
        for c in range(n, 0, -1):
            i *= c
            if show == True:
                print(f'{c}', end='')
                print(' x ' if c > 1 else ' = ', end='')
        return i
        
print(fatorial(5))