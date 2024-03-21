# Calculadora com while 

while True:
    
    number1 = input('Digite um número: ')
    number2 = input('Digite outro número: ')
    operator = input('Digite o operador ( + - / * )')
    number1_float = 0
    number2_float = 0
    
    valid_numbers = None
    
    try:
        number1_float = float(number1)
        number2_float = float(number2)
        valid_numbers = True
    except:
        valid_numbers = None
    
    if valid_numbers is None:
        print('Um ou ambos dos números digitalidos não são válido')
        continue
    
    op_allowed = '+-/*'
    
    if operator not in op_allowed:
        print ('Operador Inválido')
        continue
    
    if len(operator) >= 2:
        print ('Digite apenas5 um operador')
        continue
    
    print('Configura o resultado abaixo:')
    if operator == '+':
        print(number1_float + number2_float)
    elif operator == '-':
        print(number1_float - number2_float)
    elif operator == '/':
        print(number1_float / number2_float)
    elif operator == '*':
        print(number1_float * number2_float)

    else:
        print("")
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print('Você saiu')
    
    if sair is True:
        break