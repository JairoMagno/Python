#ALgorítimo que cálcula o valor a ser pago por um produto considerando seu preço normal:

print('Informa o preço do produto desejado e qual será sua forma de pagamento abaixo:')
preço = float(input('Preço do produto: R$'))
pagamento = int(input('Informe a forma de pagamento. Digite (1) para à vista em dinheiro ou cheque, digite (2) para à vista no cartão, digite (3) para em até 2x no cartão ou digite (4) para em até 3x ou mais no cartão: '))

if pagamento != 1 and pagamento != 2 and pagamento != 3 and pagamento != 4:
    print('Forma de pagamento NÃO encontrada. Digite entre os valor (1), (2), (3) ou (4).')
elif pagamento == 1:
    desconto = preço * 0.9
    print(f'PAGAMENTO À VISTA NO DINHEIRO OU CHEQUE. O valor do produto sofrerá um desconto de 10%, assim passando de R${preço:.2f} para R${desconto:.2f}')
elif pagamento == 2:
    desconto = preço * 0.95
    print(f'PAGAMENTO À VISTA NO CARTÃO. O valor do produto sofrerá um desconto de 5%, assim passando de R${preço:.2f} para R${desconto:.2f}')
elif pagamento == 3:
    parcelas = preço / 2
    print(f'PAGAMENTO PARCELADO EM 2X NO CARTÃO. O valor do produto não sofrerá um desconto, assim matendo-se R${preço:.2f} e sendo pago em duas parcelas de R${parcelas:.2f}.')
else:
    desconto = preço * 1.2
    quantidade = int(input(f'PAGAMENTO PARCELADO EM 3X OU MAIS NO CARTÃO. Em quantas vezes deseja parcelar? '))
    parcelas = preço / quantidade
    print(f'O valor do produto sofrerá um juros de 20%, assim passando de R${preço:.2f} para R${desconto:.2f} e sendo pago em {quantidade} parcelas de R${preço:.2f}')
print('---FIM---')
