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

    
if __name__ == '__main__':
    tuplesAndHashTable()