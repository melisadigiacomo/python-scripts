# Functions

def sumar_lista(lista): 
    ''' Realiza la sumatoria de los elementos
    de la lista.
    Pre: recibe una lista.
    Pos: devuelve la sumatoria de los elementos de la lista.
    '''
    suma = 0 # variable que almacenará la sumatoria
    for elem in lista:
        suma += elem # acumulador de elementos

    return suma 

# Llamada a la función:
numeros= [1,2,10,-5]
print(numeros)
print("La suma es: ", sumar_lista(numeros)) # La suma es:  8


def calcular_suma_prom(lista):
    'Retornar la sumatoria y el promedio de una lista.'

    suma = sumar_lista(lista) # Llamando a una fx dentro de otra fx
    prom = suma/len(lista) # Calculo el promedio 

    return suma, prom # Retona 2 valores

# Llamado a una fx que retorna 2 valores
result1,result2 = calcular_suma_prom(numeros) 
print("La sumatoria es:", result1, "y el promedio es:", result2)

# Llamado a una fx e impresión resultados sin guardar en variables
print("La sumatoria es:", calcular_suma_prom(numeros)[0], "y el promedio es:", calcular_suma_prom(numeros)[1])
