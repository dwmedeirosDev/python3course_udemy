# #Interpolação básica de strings
# nome = 'Luiz'
# preco = 100.000
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)

var = 'abc'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}.')

# Fatiamento de Strings
fatiar = 'David William'
print(fatiar[6:])
print(len(fatiar))
print (fatiar[-1:-14:-1]) # print (fatiar[::-1]) # Inverter