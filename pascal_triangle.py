# Pascal's Triangle

# Pascal's triangle is a triangular array of the binomial coefficients that arises in 
# probability theory, combinatorics, and algebra.

# Pascal's triangle is a triangular array of numbers: 
# Rows are numbered from n = 0, top to bottom.
# The values ​​in each row are listed from k = 0 (left to right).
# The values ​​at the edges of the triangle are all ones.
# Any other value is calculated by adding the two contiguous values ​​in the row above.

def pascal(n,k):
    '''Calcula el valor que se encuentra en la fila n y la columna k de 
    un triángulo de Pascal
    Pre: n y k números enteros positivos.
    Pos: devuelve el valor en la fila n y columna k.'''

    if k > n:
        print("Te encuentras fuera de los límites del triángulo de Pascal")

    else:
        #La primer columna (k=0) y la última de cada fila (k=n) devuelven siempre 1
        if k == 0 or k == n:    #Caso base
            return 1            #Condicion de salida

        else:
            #El valor está determinado por la suma de los valores de 
            #la fila anterior (n-1) en las posiciones k y (k-1)
            res = pascal((n-1), k) + pascal((n-1),(k-1))

    return res


n=5
k=2
print(f'El valor que se encuentra en la fila {n} y la columna {k} del triángulo de Pascal es: {pascal(n,k)}')
# El valor que se encuentra en la fila 5 y la columna 2 del tri�ngulo de Pascal es: 10

n=0
k=0
print(f'El valor que se encuentra en la fila {n} y la columna {k} del triángulo de Pascal es: {pascal(n,k)}')
# El valor que se encuentra en la fila 0 y la columna 0 del tri�ngulo de Pascal es: 1

n=5
k=5
print(f'El valor que se encuentra en la fila {n} y la columna {k} del triángulo de Pascal es: {pascal(n,k)}')
# El valor que se encuentra en la fila 5 y la columna 5 del tri�ngulo de Pascal es: 1

n=2
k=1
print(f'El valor que se encuentra en la fila {n} y la columna {k} del triángulo de Pascal es: {pascal(n,k)}')
# El valor que se encuentra en la fila 2 y la columna 1 del tri�ngulo de Pascal es: 2