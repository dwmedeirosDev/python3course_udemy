frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'

print (frase.count("Python"))

i=0
qtd_apareceu_mais_vezes = 0 
apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)


    i += 1
    
    print(letra_atual, quantas_vezes_letra_apareceu)