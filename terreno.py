def lista():
    print('-'*20)
    return

lista()
print('Controle de terreno')
lista()

cumprimento = float(input('Insira o cumprimento: '))
largura = float(input('Insira a largura: '))

def terreno(cumpri,lar):
    total = cumpri*lar
    return total   

final = terreno(cumprimento,largura)

lista()
print(f'o tamanho do terreno {cumprimento}x{largura} dá um total de {final}')
lista()