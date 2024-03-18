# contador = 5

# contador *= 5
# print(contador)

contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print('"Continue" para pular o 6')
        continue
        
    if contador >= 10 and contador <= 27:
        continue
    
    print(contador)
