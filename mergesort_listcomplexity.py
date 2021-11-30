# -*- coding: utf-8 -*-

# Code that calculated the execution time of merge sort algorithms based on different list complexities

import random
import numpy as np
import matplotlib.pyplot as plt
import timeit as tt

random.seed(10)

# Random list

def generar_listas(Nmax):
    listas=[]
    for i in range(Nmax):
        lista= []
        for j in range(i+1):
            lista.append(random.randint(1, 1000))
        listas.append(lista)
    return listas

# Reversed list

def reverse_lists(Nmax):
    listas=[]
    for i in range(Nmax):
        lista= []
        for j in range(i+1):
            lista.append(random.randint(1, 1000))
            lista = sorted(lista, reverse = True)
        listas.append(lista)
    return listas

# Sorted list

def sorted_lists(Nmax):
    listas=[]
    for i in range(Nmax):
        lista= []
        for j in range(i+1):
            lista.append(random.randint(1, 1000))
            lista = sorted(lista, reverse = False)
        listas.append(lista)
    return listas


## merge sort algorithm ##

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
    Realiza un experimento usando timeit para evaluar el método de ordenamiento merge
    con las listas pasadas como entrada y devuelve los tiempos de ejecución 
    para cada lista en un vector.
    Pre: El parámetro 'listas' debe ser una lista de listas.
         El parámetro 'num' indica la cantidad de repeticiones a ejecutar cada método 
         para cada lista.
    Pos: devuelve los tiempos de ejecución.
    """

    tiempos = []

    global lista

    #Evaluo cada método de ordenamiento en una nueva copia para cada iteración
    for lista in listas:
        tiempo = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())

        #Guardo el resultado
        tiempos.append(tiempo)

    #Paso los tiempos a vectores
    tiempos = np.array(tiempos)

    return tiempos


## Comparing the execution time of merge sort algorithm of different lists: graphic method

# Random lists
randomlists = generar_listas(300)
tiempo_randomlists = experimento_timeit(randomlists, 10)

# Reversed lists
reversedlists = reverse_lists(300)
tiempo_reversedlists = experimento_timeit(reversedlists, 10)

# Sorted lists
sortedlists = sorted_lists(300)
tiempo_sortedlists = experimento_timeit(sortedlists, 10)



# Grafico
plt.plot(tiempo_randomlists, label = 'Random Lists')
plt.plot(tiempo_reversedlists, label = 'Reversed Lists')
plt.plot(tiempo_sortedlists, label = 'Sorted Lists')


plt.ylabel("Execution time")
plt.title("Execution time of merge sort algorithm")
plt.xlabel("List lenght")
plt.legend()
plt.xlim(0, 300)
plt.ylim(0)
plt.show()