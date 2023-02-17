"""Algorítimo que lê um nome e mostra os seguintes itens:
1)O nome com todas as letras maiúsculas;
2)O nome com todas as letas minúsculas;
3)Quantas letras ao todo(sem consideras espaços);
4)Quantas letras tem o primeiro nome                     """

nome = input('Informe seu nome:')
mai = nome.upper() #Frase em maiúsculo
min = nome.lower() #Frase em minúsculo
lpm = nome.split() #Separando as palavras em listas
clat = len(nome) - nome.count(' ')  #Contado quantas letras temos ao todo(sem espaços)
clpm = len(lpm[0]) #Contando o tamanho da primeira palavra da lista
print('------------------------------------------------------------')
print(f'O nome todo em maiúsculo é: {mai}')
print(f'O nome todo em minúsculo é: {min}')
print(f'A quantidade de letras ao todo contando os espaços é: {len(nome)}')
print(f'A quantidade de letras ao todo sem espaço são: {clat}')
print(f'A quantidade de letras que tem no primeiro nome é: {clpm}')
print('------------------------------------------------------------') 