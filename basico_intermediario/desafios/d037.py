#Algorítimo que lê o ano de nascimento de um atleta e informa sua categoria:

from datetime import date

anoatual = date.today().year
atleta = int(input('Informe seu ano de nascimento para ser checado sua categoria: '))
if (anoatual - atleta) < 0:
    print('Não se pode ter uma idade negativa. Informe novamente seu ano de nascimento')
elif (anoatual - atleta) <= 9:
    print(f'Pele seu ano de nascimento {atleta}, o atleta tem {anoatual - atleta} e sua categoria é MIRIM.')
elif (anoatual - atleta) > 9 and (anoatual - atleta) <= 14:
    print(f'Pele seu ano de nascimento {atleta}, o atleta tem {anoatual - atleta} e sua categoria é INFANTIL.')
elif (anoatual - atleta) > 14 and (anoatual - atleta) <= 19:
    print(f'Pele seu ano de nascimento {atleta}, o atleta tem {anoatual - atleta} e sua categoria é JÚNIOR.')
elif 19 < (anoatual - atleta) <= 25:
    print(f'Pele seu ano de nascimento {atleta}, o atleta tem {anoatual - atleta} e sua categoria é SÉNIOR.')
else:
    print(f'Pele seu ano de nascimento {atleta}, o atleta tem {anoatual - atleta} e sua categoria é MASTER.')
print('---FIM---')