# -*- coding: utf-8 -*-

# Search one element

def buscar_u_elemento(lista, u):
    '''Si u está en la lista devuelve su última posición, 
    de lo contrario devuelve -1.'''
    pos = -1  # comenzamos suponiendo que e no está
    # si i no está, devuelve el -1
    for i, z in enumerate(lista): 
        if z == u:  
            pos = i  
            #Sin salir del ciclo dará la última posición encontrada para u
    return pos

# Ejemplos:
print(buscar_u_elemento([1,2,3,2,3,4],1))
#0
print(buscar_u_elemento([1,2,3,2,3,4],2))
#3
print(buscar_u_elemento([1,2,3,2,3,4],3))
#4
print(buscar_u_elemento([1,2,3,2,3,4],5))
#-1


# Search min and max value

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.'''
    m = lista[0] # Inicializo en el primer valor de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e
    return m

#Ejemplos:
print(maximo([1,2,7,2,3,4]))
#7
print(maximo([1,2,3,4]))
#4
print(maximo([-5,4]))
#4
print(maximo([-5,-4]))
#-4


# minimo()

def minimo(lista):
    '''Devuelve el mínimo de una lista, 
    la lista debe ser no vacía.'''
    m = lista[0] # Inicializo en el primer valor de la lista
    for e in lista: # Recorro la lista y voy guardando el menor
        if e<m:
            m=e
    return m

#Ejemplos:
print(minimo([1,2,7,2,3,4]))
#1
print(minimo([1,2,3,4]))
#1
print(minimo([-5,4]))
#-5
print(minimo([-5,-4]))
#-5
