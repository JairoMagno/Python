#Algorítimo que confirma se um ano é bissexto:

ano = int(input('Informe qual ano você quer checar se é bissexto: '))
condiçao = (ano % 4 == 0) and (((ano % 100) != 0) or ((ano % 400) == 0)) #So funciona para anos a partir de 1582 (Calendário Gregoriano)
#condiçao2 = (ano % 4 == 0) and ((ano % 100) == 0) and ((ano % 400) == 0)

if ano <= 1582:
    print('VALOR NÃO CÁLCULÁVEL. O cálculo so pode ser realizado para anos acima de 1582 de acordo com o Calendário Gregoriano.')
elif condiçao == True:
    print(f'O ano {ano} É um ano bissexto.')
else:
    print(f'O ano {ano} NÃO é um ano bissexto.')
print('---FIM---')