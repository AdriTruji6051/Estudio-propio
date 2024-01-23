palabra = ''
idx = 0
err = False

def M():
    global palabra, idx, err
    cCounter = 0
    dCounter = 0
    noMoreChars = False
    momenIdx = idx
    
    #Contamos cuantas c's hay para saber como vamos a avanzar
    while(cCounter != 3 and noMoreChars != True):     
        if momenIdx < len(palabra) and palabra[momenIdx] == 'c': 
            cCounter += 1
            momenIdx +=1
        else:
            noMoreChars = True

    noMoreChars = False
    if cCounter == 2:
        idx+=2 
        #Avanzamos las d's en la ultima derivada
        if idx == len(palabra): err = True
        while(dCounter != 3 and noMoreChars != True):
            if idx < len(palabra) and palabra[idx] == 'd':    
                dCounter += 1
                idx +=1
            else:
                noMoreChars = True
                err = True
               
    elif cCounter == 3:
        idx+=1
        M()
        #Avanzamos las d's en la derivada normal
        if idx == len(palabra): err = True
        if idx < len(palabra) and palabra[idx] == 'd':    
            idx +=1
        else:
            err = True
    else:
        err = True
        
def S():
    M()
    
def parser(): 
    global err, palabra, idx
    S()
    if idx < len(palabra) or idx > len(palabra): 
        err = True
    if not(err):
        print(palabra, 'PERTENECE al Lenguaje')
    else:
        print(palabra, 'NO es VALIDA al lenguaje')

print('PUTO4')
palabra = input('Dame palabra [.]=salir: ')
while palabra != '.':
    idx = 0 
    err = False
    parser()
    palabra = input('Dame palabra [.]=salir: ')