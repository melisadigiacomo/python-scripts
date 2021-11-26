# -*- coding: utf-8 -*-

# 2D random walk

# Modules
import numpy as np
import matplotlib.pyplot as plt
import random

# Function 2D random walk
def randomwalk2D(largo):
    "Caminata al azar 2D de un determinado largo (número de pasos)"

    #arrays to store the position 
    x = np.zeros(largo) 
    y = np.zeros(largo) 
    #directions
    direction=["up","down","right","left"] 

    for i in range(1, largo):
        #Random choose of the direction 
        pasos = random.choice(direction) 
        if pasos == "right":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1] 
        elif pasos == "left": 
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1] 
        elif pasos == "up": 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        else: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] - 1

    return x,y


# 2D random walk
N = 10000
x, y = randomwalk2D(N)

# Plot
plt.plot(x, y, color='orange')
plt.title('2D random walk')
plt.show()


# 3 random walks
N = 10000
a, b = randomwalk2D(N)
c, d = randomwalk2D(N)
e, f = randomwalk2D(N)

plt.plot(a, b, color= "orange")
plt.plot(c, d, color= "blue")
plt.plot(e, f, color= "green")
plt.title('Three 2D random walks')
plt.show()