# -*- coding: utf-8 -*-

# Code to compare time of the different sorting algorithms

import random
import numpy as np
import matplotlib.pyplot as plt

## merge sort algorithm ##

def merge_sort(lista):
    
    comparaciones=0
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


## Selection sort ##

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


## Insertion sort ##

def ord_insercion(lista):
    'Ordenamiento por inserción de una lista. Devuelve el número de comparaciones realizadas'

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


## Bubble sort ##

def ord_burbujeo(lista, comparaciones=0):
    '''Ordenamiento por burbujeo de una lista. Devuelve el número de comparaciones realizadas'''

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


## Comparing the 4 sorting algorithms

def total_comparaciones(N):
    ''''Calcula la cantidad de comparaciones realizadas por cada método 
    (selección, inserción, burbujeo y merge_sort) y guarda estos resultados 
    en vectores de largo N.
    Pre: N largo de la lista
    Pos: Vector con el largo y lista de vectores con la cantidad comparaciones
         para los métodos selección, inserción, burbujeo y merge_sort.'''

    #Genero un vector de 1 a N
    largo = np.arange(N)+1

    #Genero 4 vectores para guardar la cantidad de comparaciones de los 4 métodos
    comparaciones_seleccion = np.zeros(N)
    comparaciones_insercion = np.zeros(N)
    comparaciones_burbujeo = np.zeros(N)
    comparaciones_merge_sort = np.zeros(N)


    for i, n in enumerate(largo): 
        #Voy generando listas de largos n
        lista = generar_lista(n)
        #Copia las listas generadas 4 veces, una para cada método
        listas = [lista, lista.copy(), lista.copy(), lista.copy()]

        #Calculo y guardo las comparaciones de cada método
        comparaciones_seleccion[i] = ord_seleccion(listas[0])
        comparaciones_insercion[i] = ord_insercion(listas[1])
        comparaciones_burbujeo[i] = ord_burbujeo(listas[2])
        comparaciones_merge_sort[i] = merge_sort(listas[3])[1]

    #Armo una lista que contenga los 4 vectores con las comparaciones de los métodos
    comparaciones = [comparaciones_seleccion, comparaciones_insercion,
                     comparaciones_burbujeo, comparaciones_merge_sort]

    #Devuelto el vector con el largo y la lista con los vectores con la cantidad comparaciones
    return largo, comparaciones


## Comparing the 4 sorting algorithms: graphic method

largo, comps = total_comparaciones(256)
comparaciones = comps

# Grafico largo de listas vs cantidad de comparaciones promedio de los 4 métodos.
plt.plot(largo, comparaciones[0], label = 'Selection Sort Algorithm')
plt.plot(largo, comparaciones[1], label = 'Insertion Sort Algorithm')
plt.plot(largo, comparaciones[2], label = 'Bubble Sort Algorithm')
plt.plot(largo, comparaciones[3], label = 'Merge-sort Algorithm')
plt.xlabel('List lenght')
plt.ylabel('Number of comparissons')
plt.title('Sorting Algorithms Comparisson')
plt.xlim(0, 256)
plt.ylim(0, 60000)
plt.legend()
plt.show()