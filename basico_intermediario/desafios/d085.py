aluno = dict()
alunos = list()

while True:
    print('=-' * 30)
    continuar = ''
    aluno['Nome'] = str(input('Qual o nome do aluno: '))
    aluno['Média'] = float(input('Qual foi a sua média: '))
    if aluno['Média'] >= 7:
        aluno['Situação'] = 'APROVADO'
    else:
        aluno['Situação'] = 'REPROVADO'

    print(f'A situação de {aluno["Nome"]} com média {aluno["Média"]} é: {aluno["Situação"]}!')
    alunos.append(aluno.copy())
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja verificar a situação de outro aluno [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print(f'A lista completa com todos os alunos é: {alunos}')