from colorama import Fore
from time import sleep
c = (Fore.RESET,    #0 Sem cor
     Fore.GREEN,    #1 Cor verde  
     Fore.RED,      #2 Cor vermelha
     Fore.CYAN,     #3 Cor Ciano
     Fore.MAGENTA ) #4 Cor Magenta
def menu(msg, cores=0): 
    tam = len(msg) + 4
    print(f'{c[cores]}~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])
def interactiveHelp(comando):
    menu(f'Acessando o manual do comando \'{comando}\'...', 4)
    print(c[3])
    help(comando)
    print(c[0])
    

comando = ''
while True:
    menu('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        interactiveHelp(comando)
menu('ATÉ LOGO', 2)