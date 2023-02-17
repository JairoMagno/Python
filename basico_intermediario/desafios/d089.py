dados = dict()
lista = list()
cont = 1
soma = 0

while True:
    print('=-' * 10)
    continuar = ''
    dados['Nome'] = str(input(f'Qual o nome da pessoa {cont}: ')).strip().capitalize()
    while True:
        dados['Sexo'] = str(input(f'Qual seu sexo [M/F]: ')).strip().upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('Sexo inválido. Digite novamente.')
    dados['Idade'] = int(input('Qual a sua idade: '))
    soma += dados['Idade']
    lista.append(dados.copy())
    while True:
        continuar = str(input('Deseja continuar cadastrando [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Valor Inválido. Digite novamente!')
    if continuar == 'N':
        break
    cont += 1
print('=-' * 30)
print(f'- Ao total {len(lista)} pessoas foram cadastradas.')
média = soma / len(lista)
print(f'- A média de idade do grupo é de {média} anos')
print(f'- A lista contendo apenas as mulheres é: ', end='')
for c in lista: 
    if c['Sexo'] in 'F':
        print(f'[{c["Nome"]}] ', end='')
print()
print(f'- A lista contendo apenas as pessoas acima da média são: ')    
for c in lista:
    if c['Idade'] > média:
        print(f'    => {c["Nome"]} está acima da média de idade com {c["Idade"]} anos.')
