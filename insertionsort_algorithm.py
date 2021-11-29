## Insertion sort ##

import random

def ord_insercion(lista):
    '''Ordenamiento por inserción de una lista.
    Devuelve el número de comparaciones realizadas'''

    comparaciones = 0 
    
    for i in range(len(lista) - 1):
        comparaciones += 1
        
        if lista[i + 1] < lista[i]:
            p = reubicar(lista, i + 1)
            comparaciones += p    
   
    return comparaciones

def reubicar(lista, p):
    v = lista[p]
    comps = 0
    j = p
    while j > 0 and v < lista[j - 1]:
        comps += 2
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v  
    
    return comps

## Create aleatory number lists

def generar_lista(N):
    'Genera una lista de N elementos que toman valores entre 1 y 1000'
    listas= [random.randint(1, 1000) for i in range(N)]
    return listas

list1 = generar_lista(50)
sorted_list1 = ord_insercion(list1)
print(f'Number of comparissons needed to sort a list of 50 numbers with insertion sort algorithm: {sorted_list1}')