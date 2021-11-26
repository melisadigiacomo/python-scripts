# -*- coding: utf-8 -*-

# Random walk

# Modules
import numpy as np
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(1234)

# Functions
def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)
    return pasos.cumsum()


def graficar_caminatas(N,cantidad_caminatas):
    '''Grafica una cantidad de caminatas de N cantidad de pasos.
    Además grafica la caminata que más se aleja del origen (tiene en algún punto 
    de su recorrido, el punto más alejado del cero de todas las caminatas)
    y la caminata que más se acerca al origen (el punto máximo de este recorrido 
    es el que más cerca del cero se encuentra de todas las caminatas)'''

    maximos = []
    caminatas = []

    for i in range(cantidad_caminatas):
        pasos = randomwalk(N)
        caminatas.append(pasos) # Obtengo las caminatas
        maximo = max(abs(pasos))
        maximos.append(maximo) # Junto los máximos de cada caminata

    minimo = min(maximos)
    maximo = max(maximos)

    for caminata in caminatas: # Defino caminata más se aleja y más se acerca
        if max(abs(caminata)) == maximo:
           cam_max = caminata
        if max(abs(caminata)) == minimo:
           cam_min = caminata

    plt.figure(figsize=(8, 6), dpi=100)
    for caminata in caminatas:
        # Gráfico caminatas
        plt.subplot(2, 1, 1)
        plt.plot(caminata)
        plt.title(f'{cantidad_caminatas} random walks')
        plt.xlabel("time")
        plt.ylabel("Distance to origin")
        plt.ylim(-500, 500) 
        plt.yticks(np.linspace(-500, 500, 3)) # Cantidad de ticks eje y
        plt.ylim(-500 * 1.5, 500 * 1.5) # espacio alrededor eje y para visualización
        plt.xticks([]) # saca los ticks de eje x
    
        # Gráfico caminata que más se aleja en algún punto
        plt.subplot(2, 2, 3)
        plt.plot(cam_max)
        plt.axhline(y=0.5, color='black', linestyle='-')
        plt.title('The walk that is farthest from the origin')
        plt.xlabel("time")
        plt.ylabel("Distance to origin")
        plt.yticks(np.linspace(-500, 500, 3))
        plt.ylim(-500 * 1.5, 500 * 1.5)
        plt.xticks([])
    
        # Gráfico caminata que más se acerca en algún punto
        plt.subplot(2, 2, 4)
        plt.plot(cam_min)
        plt.axhline(y=0.5, color='black', linestyle='-')
        plt.title('The walk that is closest to the origin')
        plt.xlabel("time")
        plt.ylabel("Distance to origin")
        plt.ylim(-500, 500)
        plt.yticks(np.linspace(-500, 500, 3))
        plt.ylim(-500 * 1.5, 500 * 1.5)
        plt.xticks([]), plt.yticks([])

    return plt.show()

# Caminatas
N = 100000 # cantida de pasos
cantidad_caminatas = 12 # cantidad caminatas
caminatas = graficar_caminatas(N, cantidad_caminatas)