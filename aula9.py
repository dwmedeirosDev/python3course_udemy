"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    if ' ' in name:
        print (f'Seu nome contém espaço')
    else:
        print(f'Seu nome não contém espaço')
        print (f'Primeira letra do seu nome é {name[0]}')
        print (f'Últimas letra do seu nome é {name[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')
