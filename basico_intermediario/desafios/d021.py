#Algorítimo que verifica se a pessoa possui "Silva" no nome:

nome = input('Informa seu nome: ').strip()
silva = 'SILVA' in nome.upper
print(f'O nome informado possui "Silva" nele? {silva}')