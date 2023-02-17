#Algorítimo que checa se a primeira palavra de uma cidade é: "Santo"

cidade = input('Informe o nome da cidade: ').strip()
nome = (cidade[:5].upper() == 'SANTO')
print(f'O nome da cidade começa com "Santo"? {nome}')