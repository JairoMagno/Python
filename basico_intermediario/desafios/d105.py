from time import sleep
from colorama import Fore
from pacotes.numeros import numero
from pacotes.dados import tratamento
from pacotes.arquivos import *

arq = 'PessoasCadastradas.txt'

if arquivoExiste(arq) == False:
    criarArquivo(arq)

while True:
    tratamento.menu(f'{Fore.GREEN}MENU PRINCIPAL{Fore.RESET}')
    print(f'{Fore.YELLOW}1 -{Fore.RESET} {Fore.CYAN}Ver pessoas cadastradas{Fore.RESET}')
    print(f'{Fore.YELLOW}2 -{Fore.RESET} {Fore.CYAN}Cadastrar novas pessoas{Fore.RESET}')
    print(f'{Fore.YELLOW}3 -{Fore.RESET} {Fore.CYAN}Sair do sistema{Fore.RESET}')
    print('=' * 40)
    opção = numero.leiaInt(f'{Fore.YELLOW}Sua opção: {Fore.RESET}')

    if opção == 1:
        sleep(0.5)
        tratamento.menu(f'{Fore.CYAN}PESSOAS CADASTRADAS{Fore.RESET}')
        lerArquivo(arq)

    elif opção == 2:
        sleep(0.5)
        tratamento.menu(f'{Fore.YELLOW}NOVO CADASTRO{Fore.RESET}')
        nome = input(f'{Fore.YELLOW}Nome: {Fore.RESET}')
        idade = numero.leiaInt(f'{Fore.YELLOW}Idade: {Fore.RESET}')
        cadastrar(arq, nome, idade)

    elif opção == 3:
        sleep(0.5)
        tratamento.menu(f'{Fore.CYAN}Obrigado, volte sempre!{Fore.RESET}')
        break

    else:
        sleep(0.5)
        print(f'{Fore.RED}ERRO! Digite uma das 3 opções válidas.{Fore.RESET}')
