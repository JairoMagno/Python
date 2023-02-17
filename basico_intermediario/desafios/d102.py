from pacotes.numeros import numero
from pacotes.dados import tratamento

preço = tratamento.leiadinheiro('Digite o preço: R$')
numero.resumo(preço, 80, 30)