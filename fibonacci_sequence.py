############################
#    FIBONACCI SEQUENCE    #
############################

# Recursion is never the best answer:
# Example of low efficency recursion

# Fibonacci sequence: 
#F(0) = 0
#F(1) = 1
#F(n) = F(n - 1) + F(n - 2)  si n > 1

# Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)
    return res

# many of these calls are repeated, generating a total of 15 calls to the fib function,
# just to return the value fib(5).

# It is more convenient to use iterative function:

def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1): #Al debugger este ciclo, lo que sucede es los reemplazos de 
        fibn = ant1 + ant2    #los ant (dos apuntadores) que van siendo utilizados para
        ant2 = ant1           #calcular fibn
        ant1 = fibn
    return fibn


# To obtain the value of fib(n), n-1 iterations will be made.