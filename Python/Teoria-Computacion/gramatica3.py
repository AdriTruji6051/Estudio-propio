palabra = ''
idx = 0
err = False
    
def M():
    global palabra, idx, err
    bCounter = 0
    cCounter = 0
    noMoreChars = False
    momenIdx = idx
    
    #Contamos cuantas b's hay para saber como vamos a avanzar
    while(bCounter != 2 and noMoreChars != True):     
        if momenIdx < len(palabra) and palabra[momenIdx] == 'b': 
            bCounter += 1
            momenIdx +=1
        else:
            noMoreChars = True
            
    noMoreChars = False
    if bCounter == 2:
        idx += 2 
        M()
        #Avanzamos las c's en la derivada normal
        if idx == len(palabra): err = True
        while(cCounter != 2 and noMoreChars != True):
            if idx < len(palabra) and palabra[idx] == 'c':    
                cCounter += 1
                idx +=1
            else:
                noMoreChars = True
                err = True
               
    elif bCounter == 1:
        idx += 1
    
def S():
    global palabra, idx, err
    aCounter = 0
    dCounter = 0
    noMoreChars = False
    momenIdx = idx
    
    #Contamos cuantas a's hay para saber como vamos a avanzar
    while(aCounter != 4 and noMoreChars != True):     
        if momenIdx < len(palabra) and palabra[momenIdx] == 'a': 
            aCounter += 1
            momenIdx +=1
        else:
            noMoreChars = True
    
    noMoreChars = False
    if aCounter == 4:
        idx += 2
        S()
        #Avanzamos la a's en la derivada normal
        if idx < len(palabra) and palabra[idx] == 'd':    
            idx +=1
        else:
            err = True
    elif aCounter == 3:
        idx += 3
        M()
        #Avanzamos la d's en la derivada normal
        while(dCounter != 3 and noMoreChars != True):
            if idx < len(palabra) and palabra[idx] == 'd':    
                dCounter += 1
                idx +=1
            else:
                noMoreChars = True
                err = True
    
    elif aCounter == 0:
        err = True 
    
def parser(): 
    global err, palabra, idx
    S()
    if idx < len(palabra) or idx > len(palabra): 
        err = True
    if not(err):
        print(palabra, 'PERTENECE al Lenguaje')
    else:
        print(palabra, 'NO es VALIDA al lenguaje')

palabra = input('Dame palabra [.]=salir: ')
while palabra != '.':
    idx = 0 
    err = False
    parser()
    palabra = input('Dame palabra [.]=salir: ')