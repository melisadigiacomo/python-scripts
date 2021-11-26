# -*- coding: utf-8 -*-

# List inversion

def invertir_lista(lista):
    '''Recibe una lista y la develve invertida.'''
    invertida = []
    for e in lista: # Recorro la lista
        i = len(lista)
        while i > 0: # tomo el último elemento 
            i = i - 1
            invertida.append (lista.pop(i))
    return invertida

# Ejemplos
lista1 = [1, 2, 3, 4, 5]
print(lista1)
print(invertir_lista(lista1))

lista2 = ['Bogota', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(lista2)
print(invertir_lista(lista2))


# Another function for list inversion

def invertir_lista(lista):
    '''Recibe una lista y la develve invertida.'''
    invertida = []
    for e in lista: # Recorro la lista
        invertida= [e] + invertida #Agrego el elemento adelante!!
    return invertida

# Ejemplos
lista1 = [1, 2, 3, 4, 5]
print(lista1)
print(invertir_lista(lista1))

lista2 = ['Bogota', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(lista2)
print(invertir_lista(lista2))


# Another function for list inversion

def invertir_lista(lista):
    '''Recibe una lista y la develve invertida.'''
    invertida = []
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida

# Ejemplos
lista1 = [1, 2, 3, 4, 5]
print(lista1)
print(invertir_lista(lista1))

lista2 = ['Bogota', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(lista2)
print(invertir_lista(lista2))