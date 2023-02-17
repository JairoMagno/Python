#Algorítimo que calcula o quanto o salário de um funcionário vai aumentar
#Se o seu salário for maior que R$1250,00, seu aumento será de 10%. Caso seja menor que isso, aumento de 15%.

salario = float(input('Informe seu salário atual para verificar o quanto será seu aumento:'))

if salario <= 0:
    print('Não existe salário zerados ou negativos. Informe novamente!!!!')
elif salario > 1250:
    reajuste = salario * 1.1
    print(f'O seu salário terá um reajuste de 10%, sendo assim o valor igual a R${reajuste:.2f}')
else:
    reajuste = salario * 1.15
    print(f'O seu salário terá um reajuste de 15%, sendo assim igual a R${reajuste:.2f}.')