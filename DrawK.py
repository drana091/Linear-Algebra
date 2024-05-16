########################################################
# Import statements necessary for program to run
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show
ion()

########################################################
# Above code does not work depending on your IDE, use plt.show() at bottom
########################################################

########################################################
# Vertices and adjacency matrix to determine size and shape of graph
K = np.array([[.75, 1, 1, 2.25, 2.66, 1.36, 2.66, 2.25, 1, 1, .75],
              [0,  0, 3.25, 0,  0,  3.5,   7, 7, 3.75, 7, 7]])
adj = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])


########################################################
# Draw the initial K letter on a graph
f, ax1 = plt.subplots(1)
for i in range(11):
    for j in range(i):
        if adj[i, j] == 1:
            ax1.plot([K[0, i], K[0, j]], [K[1, i], K[1, j]], 'b')


######################################################
# Draw K with 45 degrees rotation counter-clockwise
phi = math.pi / 4
R = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
KR = np.matmul(R, K)
f, ax2 = plt.subplots(1)
for i in range(11):
    for j in range(i):
        if adj[i, j] == 1:
            ax2.plot([KR[0, i], KR[0, j]], [KR[1, i], KR[1, j]], 'b')


#######################################################
# Draw backward K
A = np.array([[1, 0], [0, 1]]) # Shear, set to 0
S = np.array([[-1, 0], [0, 1]])  # Scale by x-coordinate, negative so it flips
AC = np.matmul(S, A)
KC = np.matmul(AC, K)
f, ax3 = plt.subplots(1)
for i in range(11):
    for j in range(i):
        if adj[i, j] == 1:
            ax3.plot([KC[0, i], KC[0, j]], [KC[1, i], KC[1, j]], 'b')

# Code to show the graphs on screen
plt.show()
