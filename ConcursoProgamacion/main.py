#FIBONACCI ALGORITHM
def fibonacci(num):
    vari1 = 0
    vari2 = 1

    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        for i in range(num):
            respaldo = vari2
            vari2 = vari1 + vari2
            vari1 = respaldo
        return vari2
    
#print("Ingresa un numero:")
#numero = int(input())
#print(fibonacci(numero))


#--------------------------------------------------------------------------------------------------------------
#FACTORIAL
def factorial(num):
    resultado  = num
    for i in range(num-1, 1, -1):
        resultado *= i

    return resultado

print("FACTORIAL -> Ingresa un numero:")
numero = int(input())
print(factorial(numero))

#--------------------------------------------------------------------------------------------------------------
#FACTORIAL

#Para separar elementos dados en un mismo input
arr = map(int, input().split())