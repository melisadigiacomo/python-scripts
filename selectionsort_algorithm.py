## Selection sort ##

import random

def ord_seleccion(lista):
    'Ordenamiento por selección de una lista. Devuelve el número de comparaciones realizadas'

    comparaciones = 0
    n = len(lista) - 1
    while n > 0:
        p , comps = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        comparaciones += comps
        n = n - 1
    
    return comparaciones

def buscar_max(lista, a, b):
    comps = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        comps += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comps

## Create aleatory number lists

def generar_lista(N):
    'Genera una lista de N elementos que toman valores entre 1 y 1000'
    listas= [random.randint(1, 1000) for i in range(N)]
    return listas

list1 = generar_lista(50)
sorted_list1 = ord_seleccion(list1)
print(f'Number of comparissons needed to sort a list of 50 numbers with selection sort algorithm: {sorted_list1}')