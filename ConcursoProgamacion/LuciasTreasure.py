from math import sqrt

ended = True
contador = 2

n = int(input())
resultado = n

while(ended):
    res = sqrt(resultado)
    if res % int(res) != 0: 
        contador += 1
        resultado = n * contador
    else: ended = False

print(resultado)







    
