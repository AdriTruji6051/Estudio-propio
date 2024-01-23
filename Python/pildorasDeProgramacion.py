def indexing():
    telefono = "3-3-2-6-4-4-9-6-7-4"
    telefono = telefono[::2]
    print(telefono)
    
def mutabilidadInmutabilidad():
    #Al ser datos mutables, al momento de hacer una copia de la lista estamos 
    #haciendo referencia a su direccion de memoria, no haciendo una copia indepentiente de la misma
    estudiantes = ['Pepe', 'Marco', 'Amlo']
    new_estudiantes = estudiantes
    new_estudiantes.append('Adrian')
    
    print("Estudiantes\n", estudiantes, "\nNew Estudiantes\n", new_estudiantes)
    
def tuplas():
    #Tuplas son una estructura de datos inmutable que nos permite almacenar una serie datos bajo un Index.
    #La ventaja de las tuplas es que nos permiten devolver dos o mas datos por medio de una funcion
    return 'Amlo',87,'Presidente'

def extendedTuples():
    #Podemos hacer la asignacion de valores especificos de una tupla haciendo uso del Indexing, pero 
    #a la misma vez, tenemos maneras de igualar esos mismos valores de una manera mas sencilla
    
    #Manera tradicional
    variable = tuplas()
    name = variable[0]
    age = variable[1]
    grade = variable[2]
    print("Feo")
    print(name, age, grade, sep=",")
    
    #Manera elegante como Bob Esponja
    name, age, grade = tuplas()
    print("Bonito")
    print(name, age, grade, sep=",")

def oneLineSwapping(v1,v2):
    #Mediante tuplas podemos hacer cambio de variables usando una sola linea de codigo y que se vea mas elegante
    v1, v2 = v2, v1
    return v1, v2

def setSdt():
    #Una estructura de datos mutable que no permite almacenar datos de manera repetida
    #Podemos declararlos entre parentesis o con la funcion set
    mi_set = {1,2,3,4}
    mi_set = set()
    mi_set.add(1)
    mi_set.add(2)
    mi_set.add(3)
    mi_set.add(4)
    mi_set.add(5)
    mi_set.add(5)
    print("Set:\n", mi_set)
    
    #Convirtiendo una lista con numeros repeditos podemos llegar a eliminar los datos repetidos solo convirtiendola en un set
    mi_lista = [1,1,1,1,2,2,2,2,3,3,3,3,4,4]
    mi_set = set(mi_lista)
    print("Lista:\n", mi_set)
    
    #Podemos verificar si el elemento existe dentro de nuestro set de la siguiente manera
    pertenece = 4 in mi_set
    print("Pertenece?: ", pertenece)
    
    pertenece = 10 in mi_set
    print("Pertenece?: ", pertenece)
    
def dictionarios():
    #Una estructura de datos que nos permite almacenar varios datos haciendo uso de una primary key
    mi_diccionario = {
        'AMLO': ['Presidente', 63, True],
        'ENRIQUE': ['ExPresidente',45, False],
        'FOX': ['Pendejo', 99, False]
    }
    
    mi_diccionario2 = dict(AMLO = ['Presidente', 63, True], ENRIQUE = ['ExPresidente',45, False], FOX = ['Pendejo', 99, False])
    
    #Para añadir un elemento en nuestro diccionario
    mi_diccionario2['SALINAS'] = ['Ratero', 500, False]
    #Para almacenar uno exclusivo
    vari = mi_diccionario2['SALINAS']
    #Para eliminarlo
    del mi_diccionario2['SALINAS'] 
    
    #Para obtener solo las llaves del diccionario
    print(mi_diccionario2.keys())
    #Para obtener solo los valores
    print(mi_diccionario2.values())
    #Para obtener ambos
    print(mi_diccionario2.items())
    
    
if __name__ == '__main__':
    print("Hi")
