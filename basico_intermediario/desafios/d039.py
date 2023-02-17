#Algorítimo que calcula o IMC de uma pessoa e exibe seus status:

print('Informa sua Altura (em metros) e Peso (em Kg) abaixo:')
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / altura ** 2
if imc < 0:
    print('Não é possível um IMC negativo. Informe seus dados novamente!!')
elif imc < 18.5:
    print(f'Você possui um IMC de {imc:.2f}, portanto está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 25:
    print(f'Você possui um IMC de {imc:.2f}, portanto está com o PESO IDEAL.')
elif imc > 25 and imc < 30:
    print(f'Você possui um IMC de {imc:.2f}, portanto está com SOBREPESO.')
elif imc > 30 and imc < 40:
    print(f'Você possui um IMC de {imc:.2f}, portanto está com OBESIDADE.')
else:
    print(f'Você possui um IMC de {imc:.2f}, portanto está com OBESIDADE MÓRBIDA.')
print('---FIM---')