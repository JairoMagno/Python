#Verificando se o site http://pudim.com.br/ está acessível!

from urllib import request
from time import sleep
from colorama import Fore


print(f'{Fore.YELLOW}SE CONECTANDO AO SITE: http://pudim.com.br/ ...{Fore.RESET}')
sleep(2)
print('=' * 40)
try:
    site = request.urlopen('http://www.pudim.com.br/')
except:
    print(f'{Fore.RED}Não consegui acessar o site do pudim :({Fore.RESET}')
else:
    print(f'{Fore.GREEN}Consegui Acessar o site do pudim :){Fore.RESET}')
    print(site.read())

print('=' * 40)
