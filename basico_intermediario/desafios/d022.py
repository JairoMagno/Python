""" Algorítimo que verifica se: 
    1)Quantas vezes a letra 'a' está numa frase;
    2)Qual a posição em que o 'a' aparece a primeira vez;
    3)Qual a posição em que o 'a' aparece a última vez     """

frase = input('Informa uma frase: ').strip()
n1 = frase.upper().count('A')
n2 = frase.upper().find('A') + 1
n3 = frase.upper().rfind('A') + 1 #Verifica sua posição pelo lado direito
#n3 = ''.join(reversed(frase.upper()))  Inverte a ordem da frase (exemplo: ola vira ala)
#n4 = len(frase.upper()) - n3.find('A') Sabendo a primeira vez que o 'a' aparece na frase invertido, posso subtrair do tamanho da frase original e achar a última vez que a letra 'a' aparece na frase.
print('------------------------------------------------------')        
print(f'Quantas vezes a frase contém a letra "a"? {n1}')
print(f'Qual posição a letra "a" aparece a primeira vez? {n2}')
print(f'Qual posição a letra "a" aparece a última vez? {n3}') 
print('------------------------------------------------------') 