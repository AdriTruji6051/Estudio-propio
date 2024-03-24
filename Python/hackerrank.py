def percentages():
    #Number of students
    n = int(input())
    #Dictionary
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    vari = student_marks[query_name]
    percentage = 0
    for values in vari:
        percentage += values
        
    percentage = percentage / len(vari)
    print("%.2f" % percentage) 
    
def validation():
    s = input()
    print(any(i.isalnum() for i in s) )
    print(any(i.isalpha() for i in s) )
    print(any(i.isdigit() for i in s) )
    print(any(i.islower() for i in s) )
    print(any(i.isupper() for i in s) )
    
def printHacherRankLogo():
    thickness = int(input()) #This must be an odd number
    c = 'H'
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    for i in range(thickness+1):  
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
def tuplesAndHashTable():
    print('Hola, soy el de las hash tables con tuples ;)')
    #La N no nos sirve de nada, pero hacker rank la pedia xd ;-;
    n = int(input())

    Tuple1 = map(int, input().split())

    t = tuple(Tuple1)

    print(hash(t))

def swap_case(s):
    c = ''
    for a in range(len(s)):
        if(s[a].islower()): c += str(s[a].upper())
        elif(s[a].isupper): c += str(s[a].lower())
        else: c += s[a]
    return c

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)

#Las dos funciones son del mismo ejercicio
def count_substring(string, sub_string):
    timesInString = 0
    for char in range(len(string)):
        if string[char] == sub_string[0]:
            timesInString += isSubStringIn(string[char:char + len(sub_string)], sub_string)
    return timesInString

def isSubStringIn(string, sub_string):
    if string == sub_string: return 1
    else: return 0

import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

from itertools import product
def intertoolsImplem():
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(product(a,b))
    d = ''
    for t in c:
        d += str(t) + ' '
    print(d)
    
def designerDoor():
    n, m = map(int,input().split())
    for i in range(n//2):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))
    print('WELCOME'.center(m,'-'))
    for i in reversed(range(n//2)):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))
        
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

def print_rangoli(size):
    alphebeth = 'abcdefghijklmnopqrstuvwxyz'
    width = size + size -1
    chars = alphebeth[:size]
    for i in range(size -1):
        width += 2 

    for i in range(size-1,-1,-1):
        line = chars[i:]
        result = line[::-1] + line[1:]
        result = '-'.join(result)
        space = '-' * int((width - len(result)) / 2)
        print(space + result + space)
        width - 2
    for i in range(1,size,1):
        line = chars[i:]
        result = line[::-1] + line[1:]
        result = '-'.join(result)
        space = '-' * int((width - len(result)) / 2)
        print(space + result + space)

def minion_game(string):
    kevinVowel = 0
    stuartConsonant = 0
    stringLen = len(string)
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevinVowel += stringLen - i
        else:
            stuartConsonant += stringLen - i
    
    if stuartConsonant > kevinVowel:
        print(f'Stuart {stuartConsonant}')
    elif stuartConsonant < kevinVowel:
        print(f'Kevin {kevinVowel}')
    else:
        print('Draw')

def merge_the_tools(string, k):
    results = []
    indexing = 0
    for i in range(k, len(string) + k, k):
        chars = string[indexing:i]
        isInChars = set()
        newChars = []
        
        for c in chars:
            if c not in isInChars:
                newChars.append(c)
                isInChars.update(c)
            
        results.append(''.join(newChars))
        indexing += k     
    
    for r in results:
        print(r)

from itertools import permutations
if __name__ == '__main__':   
    s, k = input().split()
    r = list(permutations(list(s),int(k)))
    r.sort()
    for p in r:
        print(''.join(list(p)))