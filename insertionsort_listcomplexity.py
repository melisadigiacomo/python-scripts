# -*- coding: utf-8 -*-

# Code that calculated the execution time of insertion sort algorithms based on different list complexities

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


# Experimento usando timeit

def experimento_timeit(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de ordenamiento insertion
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
        tiempo = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())

        #Guardo el resultado
        tiempos.append(tiempo)

    #Paso los tiempos a vectores
    tiempos = np.array(tiempos)

    return tiempos


## Comparing the execution time of insertion algorithm of different lists: graphic method

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
plt.title("Execution time of insertion sort algorithm")
plt.xlabel("List lenght")
plt.legend()
plt.xlim(0, 300)
plt.ylim(0)
plt.show()