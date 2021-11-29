## Bubble Sort algorithm ##

import random

def ord_burbujeo(lista, comparaciones=0):
    '''Ordenamiento por burbujeo de una lista. 
    Devuelve el número de comparaciones realizadas'''

    hacer_intercambios = False

    for i in range(len(lista)-1):
        comparaciones +=1
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            hacer_intercambios = True

    if not hacer_intercambios:
        return comparaciones
    else:
        return ord_burbujeo(lista, comparaciones)


## Create aleatory number lists

def generar_lista(N):
    'Genera una lista de N elementos que toman valores entre 1 y 1000'
    listas= [random.randint(1, 1000) for i in range(N)]
    return listas

list1 = generar_lista(50)
sorted_list1 = ord_burbujeo(list1)
print(f'Number of comparissons needed to sort a list of 50 numbers with bubble sort algorithm: {sorted_list1}')