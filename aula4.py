number1 = input("Digite um número: ")
number2 = input("Digite outro número: ")

if number1 > number2:
    print(f"Número {number1} é maior que {number2}")
elif number2 > number1:
    print(f"Número {number2} é maior que {number1}")
else:
    print(f"Os dois números informados são iguais")
