def votação(ano):
    from datetime import date
    year = date.today().year
    idade = year - ano
    print('=-' * 20)
    if 16 <= idade <= 17 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')  
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif 18 <= idade < 65:
        print(f'com {idade} anos: VOTO OBRIGATÓRIO!')

anoNascimento = int(input('Qual seu ano de nascimento: '))
votação(anoNascimento)