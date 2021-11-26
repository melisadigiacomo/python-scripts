# Función tradicional para calcular el cuadrado de un numero

def square1(num):
  return num ** 2

print(square1(5)) # Resultado: 25

# Lambda

# Sintaxis: nombre = lambda parámetro: método
square = lambda x: x**2

print(square(3)) # 9

# Restrignida al uso de una sola expresión
# Sirven como argumento de otras funciones
# Expresión, función corta


# Lambda con map para listas

enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores) # [1, 1] [4, 8] [16, 64] [49, 343]