"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = int(input('Digite aqui um número: '))
# resto = numero % 2

# if resto == 0:
#     print('É par')
# else:
#     print('Não é par')

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horas = input('Que horas são?: ')

# try:
#     horas_int = int(horas)
#     if horas_int >= 0 and horas_int <= 11:
#         print('Bom dia')

#     elif horas_int >= 12 and horas_int <= 17:
#         print('Boa tarde')

#     elif horas_int >= 18 and horas_int <= 23:
#         print('Boa noite') 

#     else:
#         print('Não é uma hora')

# except:
#     print('Por favor digitar apenas número inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho > 1:
    
    if tamanho >= 1 and tamanho <= 4:
        print('Seu nome é curto')

    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal')

    else: 
        print('Seu nome é muito grande')

else:
    print('Digite mais de uma letra')
