def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #verificar se o arquivo existe e abrir para o modo de leitura (rt = read text)
        a.close()            #fechando
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  #Cria um arquivo de texto (wt = write text, + = criar)
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo \'{nome}\' criado com sucesso')

def lerArquivo(nome):
    from colorama import Fore
    try:
        a = open(nome, 'rt')
    except:
        print(f'{Fore.RED}Houve um erro ao ler o arquivo!!{Fore.RESET}')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos') 
    finally:
        a.close()
        
def cadastrar(arq, nome='desconhecido', idade=0):
    from colorama import Fore
    try:
        a = open(arq, 'at+')   #Será adicionado itens no arquivos (a = 'append')
    except:
        print(f'{Fore.RED}Houve um erro na abertura do arquivo!{Fore.RESET}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{Fore.RED}Houve um erro na hora de escrever os dados!{Fore.RESET}')
        else:
            print(f'Novo registro adicionado, {Fore.GREEN}\'{nome}\'{Fore.RESET}')
            a.close()

