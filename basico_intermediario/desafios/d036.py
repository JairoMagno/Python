#Algorítimo que calcula a média de um aluno e retorna se o mesmo passou por média, está em recuperação ou foi pra final:

from colorama import Fore

print('Informe suas duas notas para o sistemas verificar sua situação:')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 0 or media > 10:
    print(f'Não é possível ter médias negativas ou acima de 10! Informe suas notas novamente!')
elif media >= 7:
    print(f'{Fore.GREEN}PARABÉNS! Você foi aprovado com uma média de {media:.2f}{Fore.RESET}')
elif media >= 5 and media < 7:
    print(f'{Fore.YELLOW}AINDA NÃO! Você está em recuperação com uma média de {media:.2f}. Estude mais{Fore.RESET}!')
elif media < 5:
    print(f'{Fore.RED}REPROVADO! Você foi reprovado com uma média de {media:.2f}. Estude mais próximo ano!{Fore.RESET}')
print('---FIM---')
