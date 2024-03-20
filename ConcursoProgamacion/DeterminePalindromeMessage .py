
n = int(input())

palabra = str(input())
palabra = list(palabra)

datos = []
for i in range(len(palabra)):
    existe = False
    tamDatos = len(datos)
    for d in range(tamDatos):
        if datos[d][0] == palabra[i]:
            datos[d][1] += 1
            existe = True
    if existe == False:
        datos.append([palabra[i], 1])

pares = 0
impares = 0
for d in range(len(datos)):
    if datos[d][1] % 2 ==0: pares +=1
    else: impares += 1 

if(pares >= 1 and impares <= 1): print("YES")
else: print("NO")