# RECURSION

# Recursive function: a function that calls itself

# Factorial recursive function

def factorial(n):
    """Precondición: n entero positivo.
       Devuelve: n!"""
    if n == 1: # base condition
        return 1
    return n * factorial(n - 1)

print(factorial(1)) #1
print(factorial(3)) #6

# Define a base condition that stops the recursion or else the function calls itself infinitely.
# Arguments must comply the pre-condition


# Recursive and iterative algorithm

# Any recursive algorithm can be expressed as iterative and vice versa. 

# Factorial iterative function

def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact


# Generally recursive versions of algorithms use more memory
# (since the execution stack is stored in memory) but they tend to be more elegant


# Recursive power function

def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1                        #Potencia 0 da 1, caso base

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)         #Cada recursión me acerca al caso base, n==1
        return p * p                    #b^n = b^(n/2) * b^(n/2)
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)   #Cada recursión me acerca al caso base, n==1
        return p * p * b                #Multiplico b^((n-1)/2) * b^((n-1)/2) * b^1

print(potencia(2, 10)) #1024
print(potencia(3, 3)) #27
print(potencia(5, 0)) #1

#potencia(2, 10)
#  potencia(2, 5)
#    potencia(2, 2)
#      potencia(2, 1)
#        potencia(2, 0)
#          return 1
#        return 1 * 1 * 2
#      return 2 * 2
#    return 4 * 4 * 2
#  return 32 * 32
#return 1024


# Iterative power function

def potencia(b, n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    pila = []                   #Tengo que simular la pila de llamadas a las funciones
    while n > 0:
        if n % 2 == 0:
            pila.append(True)   #Apilar si el valor es par
            n //= 2
        else:
            pila.append(False)  #Apilar si el valor es impar
            n = (n - 1) // 2

    p = 1
    while pila:
        es_par = pila.pop()     #Acá tengo que desapilar, ir para atras
        if es_par:              #Par: Multiplico b^(n/2) * b^(n/2)
            p *= p
        else:                   #Impar: Multiplico b^((n-1)/2) * b^((n-1)/2) * b^1
            p *= p * b

    return p


# Three tips for recursion:

# Base case: define one or more base cases according to our problem that stop the recursion.
# Recursion case: case that is going to make the recursive call.
# Convergence: the reduction made in the recursive case needs to converge to the base cases, so that the recursion ever ends.