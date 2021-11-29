# -*- coding: utf-8 -*-

# Code that calculated the execution time of different sorting algorithms

import random
import numpy as np
import matplotlib.pyplot as plt
import timeit as tt

random.seed(10)

## Selection sort algorithm ##

def ord_seleccion(lista):
    'Ordenamiento por selección. Devuelve lista ordenada.'
    n = len(lista) - 1   
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return lista
        
def buscar_max(lista, a, b):
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

## Insertion sort algorithm ##

def ord_insercion(lista):
    'Ordenamiento por inserción. Devuelve lista ordenada.'
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista

        
def reubicar(lista, p):
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

## Bubble sort algorithm ##

def ord_burbujeo(lista, comparaciones=0):
    'Ordenamiento por burbujeo. Devuelve la lista ordenada.'
    hacer_intercambios = False
    for i in range(len(lista)-1):
        comparaciones +=1
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            hacer_intercambios = True
    if not hacer_intercambios:
        return lista
    else:
        return ord_burbujeo(lista, comparaciones)

## merge_sort algorithm ##

def merge_sort(lista):
    'Ordenamiento merge sort. Devuelve la lista ordenada.'
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

# Experimento usando timeit

def experimento_timeit(listas, num):
    """
    Realiza un experimento usando timeit para evaluar los métodos de ordenamiento
    con las listas pasadas como entrada y devuelve los tiempos de ejecución 
    para cada lista en un vector.
    Pre: El parámetro 'listas' debe ser una lista de listas.
         El parámetro 'num' indica la cantidad de repeticiones a ejecutar cada método 
         para cada lista.
    Pos: devuelve los tiempos de ejecución de selección, inserción, burbujeo y merge sort.
    """

    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge_sort = []
    
    global lista
    
    #Evaluo cada método de ordenamiento en una nueva copia para cada iteración
    for lista in listas:
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_merge_sort = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
       
        #Guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge_sort.append(tiempo_merge_sort)

    #Paso los tiempos a vectores
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge_sort = np.array(tiempos_merge_sort)

    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge_sort

# Lists

def generar_listas(Nmax):
    listas=[]
    for i in range(Nmax):
        lista= []
        for j in range(i+1):
            lista.append(random.randint(1, 1000))
        listas.append(lista)
    return listas


## Comparing the execution time of 4 sorting algorithms: graphic method

# Corro las funciones para generar las listas y calcular los tiempos
listas=generar_listas(256)
tiempos_metodos = experimento_timeit(listas,2)

# Grafico
plt.plot(tiempos_metodos[0], label = 'Selection Sort Algorithm')
plt.plot(tiempos_metodos[1], label = 'Insertion Sort Algorithm')
plt.plot(tiempos_metodos[2], label = 'Bubble Sort Algorithm')
plt.plot(tiempos_metodos[3], label = 'Merge-sort Algorithm')

plt.ylabel("Execution time")
plt.title("Execution time of sorting algorithms")
plt.xlabel("List lenght")
plt.legend()
plt.xlim(0, 256)
plt.ylim(0)
plt.show()