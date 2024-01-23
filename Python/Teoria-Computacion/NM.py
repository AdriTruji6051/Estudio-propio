palabra = ''
idx = 0 #INDICE QUE RECORRERA LA CADENA 
err = False 

def S():
    global palabra, idx, err, contador
    c = ''  # ALMACENA LA LETRA ACTUAL DE LA CADENA 
    contador = 0  #VARIABLE PARA CONTAR EL NUMERO DE CARACTERES

    while idx < len(palabra) and len(palabra) > 12 and palabra[idx] == 'a': 
        contador += 1
        idx += 1

    if contador % 2 != 1:
        err = True
        print('Se a al inicio')
        return
    if idx < len(palabra) and palabra[idx] == 'a':
        S()

    #SE LLAMA A LA FUNCION M 
    M()
    
    c = ''  # ALMACENA LA LETRA ACTUAL DE LA CADENA 
    contador = 0  #VARIABLE PARA CONTAR EL NUMERO DE d

    while idx < len(palabra) and palabra[idx] == 'd':
        contador += 1
        idx += 1

    if contador %1 != 0:
        err = True
        print('Se a al inicio')
        return

def M():
    global palabra, idx, err, contador
    c = ''  # ALMACENA LA LETRA ACTUAL DE LA CADENA 
    contador = 0  #VARIABLE PARA CONTAR EL NUMERO DE b

    while idx < len(palabra) and palabra[idx] == 'b':
        contador += 1
        idx += 1
    if contador % 1 == contador:
        err = True
        print('Se a al inicio')
        return
    if idx < len(palabra) and palabra[idx] == 'b':
        M()
        
    c = ''  # ALMACENA LA LETRA ACTUAL DE LA CADENA 
    contador = 0  #VARIABLE PARA CONTAR EL NUMERO DE c

    while idx < len(palabra) and palabra[idx] == 'c':
        contador += 1
        idx += 1

    if contador % 2 != 1 :
        err = True
        print('Se a al inicio')
        return

def parser(): 
    global err, palabra, idx
    S()
    if idx < len(palabra): 
        err = True
    if not(err):
        print(palabra, 'PERTENECE al Lenguaje')
    else:
        print(palabra, 'NO es VALIDA al lenguaje')


idx = 0 
palabra = input('Dame palabra [.]=salir: ')
while palabra != '.':
    parser()
    idx = 0
    err = False
    palabra = input('Dame palabra [.]=salir: ')