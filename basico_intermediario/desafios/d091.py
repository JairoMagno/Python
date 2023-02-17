def terreno(largura, comprimento):
    área = largura * comprimento
    print(f'A área do terreno {largura:.1f}x{comprimento:.1f} é de {área:.1f}m²')    

print('=-' * 30)
print('     Controle de Terreno     ')
print('=-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
terreno(largura, comprimento)
