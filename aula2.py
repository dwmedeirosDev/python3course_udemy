a = "A"
b = "B"
c = "1.1"
formato = "aaa"

print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

print(2**10)

nome = input('Qual seu nome? ')
print(f'O seu nome é: {nome}')

number1 = input('Digite um número: ')
number2 = input('Digite outro número: ')

int_number1 = int(number1)
int_number2 = int(number2)

soma = int_number1 + int_number2

print(f'A soma dos números digitados é: {soma}')