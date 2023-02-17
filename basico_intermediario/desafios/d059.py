#Algorítimo que calcula a Sequência de Fibonacci:

from colorama import Fore

print(f'Bem vindo a calculadora para a {Fore.GREEN}Sequência de Fibonacci!{Fore.RESET}')
limite = int(input(f'Quantos {Fore.RED}TERMOS{Fore.RESET} você deseja calcular a {Fore.GREEN}Sequência de Fibonacci!{Fore.RESET}: '))

while limite <= 0:
    limite = int(input(f'A {Fore.GREEN}Sequência de Fibonacci!{Fore.RESET} só aceita números naturais maiores que 0. Digite Novamente:')) 

t1 = 1
tn = 0
antecessor = 0
contagem = 0
soma = 0

print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')

print(f'{Fore.GREEN}{t1}{Fore.RESET} ⇀ ', end='')
while contagem < limite - 1:
    tn = t1 + antecessor  
    print(f'{Fore.GREEN}{tn} ⇀ ', end='')
    antecessor = t1
    t1 = tn
    contagem +=1
    soma += tn       
print(f' FIM{Fore.RESET}')
print(f'{Fore.MAGENTA}-=' * 20)
print(f'{Fore.RESET}', end='')
print(f'A soma total da {Fore.GREEN}Sequência de Fibonacci!{Fore.RESET} com {Fore.GREEN}{limite}{Fore.RESET} termos é: {Fore.GREEN}{soma + 1}{Fore.RESET}')
