#suma y resta Enteros
ERR = -1
I = -1
D = 1
N = 0
matran=[
    #1   *    .    x    #     =
    [1,  12 , 9  , ERR, ERR, ERR], #0
    [1  ,1  , 1  , ERR, ERR, 2  ], #1
    [3,  12 , ERR, ERR, ERR, ERR], #2
    [3, ERR,  3  , 3,   4  , 3  ], #3
    [4, ERR,  4  , ERR, ERR, 5  ], #4
    [3  ,6,   ERR, 5  , ERR, ERR], #5
    [ERR,ERR, ERR,  6,  ERR ,  7], #6
    [7  ,7  , 7,   ERR, 8  , ERR], #7
    [1,  15,  9, ERR, ERR  , ERR], #8
    [9,  9  , ERR, ERR, 10  ,  9], #9
    [10 ,10 , ERR, ERR, 11 , 10 ], #10
    
    [1,  ERR, ERR, ERR, ERR, ERR], #11
    [12, ERR, 12 , ERR, 13 , ERR], #12
    [13 ,13,   13, ERR, ERR, 14 ], #13
    [ERR,ERR, ERR, ERR, 14  ,ERR], #14 ACEPTOR
    [15 ,ERR, ERR, ERR, ERR, 16 ], #15
    [16, ERR, 16,  ERR, 17 , ERR], #16
    [18, ERR, 34, ERR, ERR , ERR], #17
    [19, ERR, 34, ERR, ERR , ERR], #18
    [20, ERR, 34, ERR, ERR , ERR], #19
    [21, ERR, 34, ERR, ERR , ERR], #20
    
    [22, ERR, 34, ERR, ERR , ERR], #21
    [23, ERR, 34, ERR, ERR , ERR], #22
    [24, ERR, 34, ERR, ERR , ERR], #23
    [25, ERR, 34, ERR, ERR , ERR], #24
    [26, ERR, 34, ERR, ERR , ERR], #25
    [27, ERR, 34, ERR, ERR , ERR], #26
    [27, ERR, 28 ,ERR, ERR , ERR], #27
    [30, ERR, ERR, 29 , ERR, ERR], #28
    [ERR,ERR, ERR, 29,  31,  ERR], #29
    [30 ,ERR, ERR, 32 , ERR, ERR], #30
    
    [ERR,ERR, ERR, ERR, 31 , ERR], #31 ACEPTOR
    [ERR,ERR, ERR, 32 , 33 , ERR], #32
    [18, ERR, ERR,33,   ERR, ERR], #33
    [ERR, ERR, ERR,34,   35, ERR], #34
    [ERR,  ERR,   ERR,   35, ERR]  #35 ACEPTOR
]

matmov = [
   #1    *    .    x    #   =
    [D, I, D, N, N, N], #0
    [D, D, D, N, N, I], #1
    [D, I, N, N, N, N], #2
    [D, N, D, D, I, D], #3
    [I, N, I, N, N, I], #4
    [D, D, N, I, N, N], #5
    [N, N, N, D, N, I], #6
    [I, I, I, N, D, N], #7
    [D, D, D, N, N, N], #8
    [D, D, N, N, I, D], #9
    [I, I, N, N, D, I], #10
    [D, N, N, N, N, N], #11
    [I, N, I, N, D, N], #12
    [D, D, D, N, N, D], #13
    [N, N, N, N, N, N], #14
    [D, N, N, N, N, D], #15
    [D, N, D, N, I, N], #16
    [I, N, D, N, N, N],  #17
    [I, N, D, N, N, N], #18
    [I, N, D, N, N, N], #19
    [I, N, D, N, N, N], #20
    [I, N, D, N, N, N], #21
    [I, N, D, N, N, N], #22
    [I, N, D, N, N, N], #23
    [I, N, D, N, N, N], #24
    [I, N, D, N, N, N], #25
    [I, N, D, N, N, N], #26
    [I, N, D, N, N, N], #27
    [D, N, N, D, N, N], #28
    [N, N, N, D, I, N],  #29
    [D, N, N, D, N, N], #30
    [N, N, N, N, N, N], #31
    [N, N, N, D, I, N], #32
    [I, N, N, I, N, N], #33
    [N, N, N, D, I, N], #34
    [N, N, N, N, N, N] #35
]

def colCar(x):
    global ERR
    if x == '1': return 0
    if x == '*': return 1
    if x == '.': return 2
    if x == 'x': return 3
    if x == '#': return 4
    if x == '=': return 5
    print("Error Simbolo Ilegal en RO", x)
    return ERR

matesc = [
   #1    *    .    x    #   =
    ['#','*','#', 'x', '#', '='], #0
    ['1','*','.', 'x', '#', '='], #1
    ['x','*','.', 'x', '#', '='], #2
    ['1','*','.', 'x', '1', '='], #3
    ['1','*','.', 'x', '#', '='], #4
    ['x','*','.', 'x', '#', '='], #5
    ['1','*','.', '1', '#', '='], #6
    ['1','*','.', 'x', '#', '='], #7
    ['#','#','#', 'x', '#', '='], #8
    ['1','*','.', 'x', '.', '='], #9
    ['1','*','.', 'x', '#', '='], #10
    ['#','*','.', 'x', '#', '='], #11
    ['1','*','.', 'x', '#', '='], #12
    ['#','#','#', 'x', '#', '#'], #13
    ['1','*','.', 'x', '#', '='], #14
    ['#','*','.', 'x', '#', '#'], #15
    ['1','*','.', 'x', '#', '='], #16
    ['x','*','.', 'x', '#', '='],  #17
    ['x','*','.', 'x', '#', '='], #18
    ['x','*','.', 'x', '#', '='], #19
    ['x','*','.', 'x', '#', '='], #20
    ['x','*','.', 'x', '#', '='], #21
    ['x','*','.', 'x', '#', '='], #22
    ['x','*','.', 'x', '#', '='], #23
    ['x','*','.', 'x', '#', '='], #24
    ['x','*','.', 'x', '#', '='], #25
    ['x','*','.', 'x', '#', '='], #26
    ['1','*','1', 'x', '#', '='], #27
    ['.','*','.', '.', '#', '='], #28
    ['1','*','.', '#', '#', '='],  #29
    ['1','*','.', '1', '#', '='], #30
    ['1','*','.', 'x', '#', '='], #31
    ['1','*','.', 'x', '#', '='], #32
    ['x','*','.', '#', '#', '='], #33
    ['1','*','.', '1', '#', '='], #34
    ['1','*','.', 'x', '#', '='] #35
]

def turing():
    global ERR, entrada
    if entrada == '-': entrada = '#'
    cinta = '#'+entrada+'##########################'
    idx = 1
    estado = 0
    print('Cinta=', cinta)
    while idx < len(cinta) and estado != ERR and estado != 14 and estado != 31 and estado != 35:
        c = cinta[idx]
        col = colCar(c)
        if col >=0 and col <= 5 and estado != ERR:
            cinta = cinta[:idx] + matesc[estado][col] + cinta[idx+1:]
            idx = idx + matmov[estado][col]
            estado = matran[estado][col]
            print(cinta, 'idx=', idx, 'estado=', estado)
        else: estado = ERR
    
    if estado != ERR and (estado == 14 or estado == 31 or estado == 35):
        print('Cinta=', cinta)
    else:
        print(entrada, 'NO ES VALIDA en lenguaje')

if __name__ == '__main__':
    entrada = input('Dame entrada MULTIPLICACION :) [.]=Salir: ')
    while entrada != '.':
        idx = 1
        turing()
        entrada = input('Dame entrada [.]=Salir: ')
