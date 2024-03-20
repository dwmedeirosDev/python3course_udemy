# Calculadora com while 

while True:
    
    number1 = input('Digite um número: ')
    number2 = input('Digite outro número: ')
    operator = input('Digite o operador ( + - / * )')
    
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
    
    op_allowed = '+-/*)'
    
    if operator not in op_allowed:
        print ('Operador Inválido')
        continue
    
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break