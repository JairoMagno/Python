#Algóritimo que verifica se um homem está na hora de alistar ao exército:

from datetime import date

ano = date.today().year 
idade = int(input(f'Informe qual idade você terá no ano de {ano}: '))
if idade < 0:
    print('Não existem anos negativos!!! Informe novamente sua idade.')
elif idade == 18:
    print(f'HORA DE SE ALISTAR!! Você terá {idade} anos em {ano}, portanto você está apto para o alistamento militar!! ')
elif idade <= 18:
    condiçao = 18 - idade
    ano2 = condiçao + ano
    print(f'Você ainda não cumpre os requisitos para se alistar! Ainda faltam {condiçao} anos para poder se alistar, ou seja, no ano de {ano2}.')
else:
    condiçao = idade -18
    ano2 = ano - condiçao
    print(f'Você ja passou do prazo para alistamente. O seu alistamente ocorreu há {condiçao} anos, ou seja, no ano de {ano2}')
print('---FIM---')