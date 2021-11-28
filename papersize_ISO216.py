# -*- coding: utf-8 -*-

# ISO 216 paper sizes and recursion

def hojas_ISO(N):
    '''Función recursiva que devuelve el ancho y el largo de la hoja A(N).
    Pre: N mayor a 0
    Pos:devuelve el ancho y el largo de la hoja A(N)'''

    if N == 0: #Caso baso, hoja A0
        ancho = 841
        largo = 1189
    else:
        medidas = hojas_ISO(N-1)    #Caso recursivo
        ancho = medidas[1]//2       #Ancho= divisón entera a la mitad del largo de la hoja anterior
        largo = medidas[0]          #Largo= el ancho de la hoja anterior
    return ancho, largo

#Estándar A4
N=4
print(f'Según la norma ISO 216, el tamaño de papel de una hoja A{N} es:')
print(f'Ancho: {hojas_ISO(N)[0]} mm')
print(f'Largo: {hojas_ISO(N)[1]} mm')

#Hoja A0, caso base
N=0
print(f'Según la norma ISO 216, el tamaño de papel de una hoja A{N} es:')
print(f'Ancho: {hojas_ISO(N)[0]} mm')
print(f'Largo: {hojas_ISO(N)[1]} mm')

#Hoja A12
N=12
print(f'Según la norma ISO 216, el tamaño de papel de una hoja A{N} es:')
print(f'Ancho: {hojas_ISO(N)[0]} mm')
print(f'Largo: {hojas_ISO(N)[1]} mm')

#Hoja A10
N=10
print(f'Según la norma ISO 216, el tamaño de papel de una hoja A{N} es:')
print(f'Ancho: {hojas_ISO(N)[0]} mm')
print(f'Largo: {hojas_ISO(N)[1]} mm')