## merge-sort algorithm ##

import random

def merge_sort(lista):
    
    comparaciones = 0

    if len(lista) < 2:
        lista_nueva = lista 
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        der = merge_sort(lista[medio:])[0]
        lista_nueva, comps = merge(izq, der)
        comparaciones += comps

    return lista_nueva, comparaciones

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    comps=0
    
    while (i < len(lista1) and j < len(lista2)):
        comps += 2
        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
           
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comps


## Create aleatory number lists

def generar_lista(N):
    'Genera una lista de N elementos que toman valores entre 1 y 1000'
    listas= [random.randint(1, 1000) for i in range(N)]
    return listas

lista1 = generar_lista(50)
print(lista1)

sorted_list1 = merge_sort(lista1)
print(f'Sorted list: {sorted_list1[0]}')
print(f'Number of comparissons needed to sort a list of 50 numbers with merge-sort algorithm: {sorted_list1[1]}')