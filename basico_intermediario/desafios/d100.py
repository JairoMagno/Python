def turma(* notas, sit=False):
    """Função que recebe n notas e mostra na tela um dicionário com algumas informações

    Args:
        sit (booleano, opcional): Valor opcional. Caso sit=True, adicionará também a situação da média da turma.

    Returns:
        _type_: retorna na tela o dicionário com informações do total de notas, a maior nota, a menor nota, a média e a situação 
                da média da turma (Apenas se sit=True).
    """
    conjunto = dict()
    conjunto['Total'] = len(notas)
    conjunto['Maior'] = max(notas)
    conjunto['Menor'] = min(notas)
    média = sum(notas) / len(notas)
    conjunto['Média'] = média
    if sit == True:
        if média >= 7:
            conjunto['Situação'] = 'BOA'
        elif 5 <= média < 7:
            conjunto['Situação'] = 'RAZOÁVEL'
        else:
            conjunto['Situação'] = 'RUIM'
    return conjunto

notas = turma(10, 5, 9, 8, sit=True)
print(notas)