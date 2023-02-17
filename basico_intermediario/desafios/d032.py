#Algorítmo que aprova um empréstimo de uma casa:

from colorama import Fore, Back, Style

print(f'{Fore.MAGENTA}Será calculado se o empréstimo para uma pessoa será aprovado de acordo com o valor da casa, o salário da pessoa e em quantos anos será pago!{Fore.RESET}')
casa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('De quanto é o seu salário? R$'))
anos = float(input('Em quantos anos você pretende pagar toda a casa? '))
condiçao = casa / ( salario * anos * 12 )
emprestimo = condiçao * salario

if condiçao >= 0.3:
    print(f'{Fore.RED}EMPRÉSTIMO NEGADO!{Fore.RESET} Com essas condições você iria precisar pagar uma parcela de acima de {Fore.RED}30%{Fore.RESET}, ou seja, {Fore.RED}{condiçao * 100:.2f}% (R${emprestimo:.2f}){Fore.RESET} do seu salário atual!')
else:
    print(f'{Fore.GREEN}EMPRÉSTIMO ACEITO!{Fore.RESET} Com essas condições você iria precisar pagar uma parcela inferior à {Fore.GREEN}30%{Fore.RESET}, ou seja, {Fore.GREEN}{condiçao * 100:.2f}% (R${emprestimo:.2f}){Fore.GREEN} seu salário atual!')
print(f'{Fore.CYAN}---FIM---{Fore.RESET}')