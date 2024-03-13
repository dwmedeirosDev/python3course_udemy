print("Hello, World")
# Comentário
"""Não é comentário"""

# print(type(1))
# print(type(0.1))
# print(type("David"))
# print(type(10==10))

nome_completo = "David Medeiros"
print(nome_completo)
idade = 30
verificacao = idade >= 18

print("Nome:", nome_completo,
      "Idade:", idade,
      "É maior de idade? :", verificacao)

print (10 % 5 == 1)
print (10 % 5 == 0)

print((1+1) ** (5+5))


name = "David" #nome
height = 1.76 #altura
weight = 77 #peso
imc = weight / (height*height) #Índice de Massa Corporal

print("Meu nome é:", name)
print("Eu tenho:", height, "de altura")
print("Eu peso:", weight, "kg")
print("Meu IMC é:", imc)

# f-strings (Formatação)
linha_1 = f"Meu nome é {name}, tenho {height:.2f} de altura e peso {weight}kg"
print (linha_1)

linha_2 = f"Meu imc é {imc:.2f}"
print (linha_2)

# time = "Flamengo"
# data = 1

# print(time)
# print(type(data))

# time = 1.2

# print(type(time))