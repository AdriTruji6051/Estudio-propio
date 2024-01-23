# <s>::=a<s>b | ab
palabra = ''
idx = 0
err = False

def S():
    global palabra, idx, err
    c = ''
    if idx < len(palabra):
        c = palabra[idx]
    idx += 1
    if c == 'a':
        if idx < len(palabra): 
            c = palabra[idx]
        if c != 'a' and c != 'b':
            err= True
            print('Se esperaba a o b y llego', c)
        elif c == 'a': 
            S()
            c = ''
            if idx < len(palabra):
               c = palabra[idx]
            idx += 1
            if c != 'b': 
                print('Se esperaba b y llego ', c)
                err = True
        else:
            idx += 1
     
    
      
def parser(): 
    global err
    S()
    if idx < len(palabra): err = True
    if not(err):
        print(palabra, 'PERTENECE al Lenguaje')
    else:
        print(palabra, 'NO es VALIDA al lenguaje')

if __name__ == '__main__':
    idx = 0 
    palabra = input('Dame palabra [.]=salir: ')
    while palabra != '.':
        parser()
        idx = 0
        err = False
        palabra = input('Dame palabra [.]=salir: ')