#suma y resta Enteros
I = -1
ERR = -1
D = 1
N = 0
matran=[
    #1   +    -    #
    [0,  1,   4,   10], #0
    [1,  ERR, ERR, 2  ], #1
    [3,  ERR, ERR, ERR], #2
    [ERR,ERR, 10,  3  ], #3
    [4,  ERR, ERR, 5  ], #4
    [6,  ERR, 3,   ERR], #5
    [6,  ERR, 6,   7  ], #6
    [8,  ERR, 3,   ERR], #7
    [9,  ERR, 3,   ERR], #8
    [9,  ERR, 9,   5  ], #9
    [ERR,ERR, ERR, 10]  #10
]
matmov=[
    #1   +    -    #
    [D,  D,   I,   D], #0
    [D,  N,   N,   I], #1
    [D,  N,   N,   N], #2
    [N,  N,   D,   I], #3
    [I,  N,   N,   D], #4
    [D,  N,   D,   N], #5
    [D,  N,   D,   I], #6
    [I,  N,   D,   N], #7
    [I,  N,   D,   N], #8
    [I,  N,   I,   D], #9
    [N,  N,   N,   N]  #10
]

def colCar(x):
    global ERR
    if x == '1': return 0
    if x == '+': return 1
    if x == '-': return 2
    if x == '#': return 3
    print("Error Simbolo Ilegal en RO", x)
    return ERR

matesc=[
    #1    +   -    #
    ['1','1','-', '#'], #0
    ['1','+','-', '#'], #1
    ['#','+','-', '#'], #2
    ['1','+','#', '#'], #3
    ['1','+','-', '#'], #4
    ['#','+','-', '#'], #5
    ['1','+','-', '#'], #6
    ['#','+','1', '#'], #7
    ['1','+','#', '#'], #8
    ['1','+','-', '#'], #9
    ['1','+','-', '#']  #10
]

def turing():
    global ERR, entrada
    if entrada == '-': entrada = '#'
    cinta = '#'+entrada+'#'
    idx = 1
    estado = 0
    print('Cinta=', cinta)
    while idx < len(cinta) and estado != ERR and estado != 3 and estado != 10:
        c = cinta[idx]
        col = colCar(c)
        if col >=0 and col <= 3 and estado != ERR:
            cinta = cinta[:idx] + matesc[estado][col] + cinta[idx+1:]
            idx = idx + matmov[estado][col]
            estado = matran[estado][col]
            print(cinta, 'idx=', idx, 'estado=', estado)
        else: estado = ERR
    
    if estado != ERR and (estado == 3 or estado == 10):
        print('Cinta=', cinta)
    else:
        print('Error en operacion')

if __name__ == '__main__':
    entrada = input('Dame entrada PA SUMAR O RESTAR [.]=Salir: ')
    while entrada != '.':
        idx = 1
        turing()
        entrada = input('Dame entrada [.]=Salir: ')
