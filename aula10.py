# number = input("Digite um número: ") #retorna uma string
# converter = int(number)
# #print(type(converter))
# print(f'O dobro de {number} é {converter*2}')

numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro do {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número')