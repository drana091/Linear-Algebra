# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:41:57 2021

@author: Dhruv Rana
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import plot, ion, show

D = np.array([[3,5,5,3,3,5,5,3], 
              [1,1,0,0,1,1,0,0], 
              [5,5,5,5,4,4,4,4],
              [1,1,1,1,1,1,1,1]])

C = np.array([[0,1,0,1,1,0,0,0],
              [1,0,1,0,0,1,0,0],
              [0,1,0,1,0,0,1,0],
              [1,0,1,0,0,0,0,1],
              [1,0,0,0,0,1,0,1],
              [0,1,0,0,1,0,1,0],
              [0,0,1,0,0,1,0,1],
              [0,0,0,1,1,0,1,0]])

P1 = np.array([[1,0,0,0],
               [0,1,0,0],
               [0,0,0,0],
               [0,0,-0.1,1]])
PD1 = np.matmul(P1, D)
for j in range (8):
    PD1[:,j] = PD1[:,j] / PD1[3,j]
f, ax1 = plt.subplots(1)

for i in range (8):
    for j in range(i):
        if C[i,j] == 1:
            ax1.plot([PD1[0,i], PD1[0,j]], [PD1[1,i], PD1[1,j]], 'r-')
ax1.set_title('Center at (0,0,10)')
ax1.axis('off')
plt.show()

##############################
#Projecttion center (10,5,10)

P2 = np.array([[1,0,-1,0],
               [0,1,-.5,0],
               [0,0,0,0],
               [0,0,-0.1,1]])
PD2 = np.matmul(P2, D)
#for j in range (8):
#    PD2[:,j] = PD2[:,j] / PD2[3,j]
PD2[0,:] = PD2[0,:] / PD2[3,:]
PD2[1,:] = PD2[1,:] / PD2[3,:]

f, ax2 = plt.subplots(1)

for i in range (8):
    for j in range(i):
        if C[i,j] == 1:
            ax2.plot([PD2[0,i], PD2[0,j]], [PD2[1,i], PD2[1,j]], 'r-')
ax2.set_title('Center at (10,5,10)')
ax2.axis('off')

# Zoom in by 150% and projection at (0,10,25)

P6 = np.array([[1.5, 0, 0, 0],
              [0, 1.5, 0, 0],
              [0, 0, 1.5, 0],
              [0, 0, 0, 1]])  # Projection matrix

#test = np.matmul()
PD6 = np.matmul(P6,PD2)


PD6[0,:] = PD6[0,:] / PD6[3,:]
PD6[1,:] = PD6[1,:] / PD6[3,:]

f, ax6 = plt.subplots(1)

ax6.plot(PD6[0, :], PD6[1, :], 'b.')
for i in range(8):
   for j in range(i):
       if C[i, j] == 1:
           ax6.plot([PD6[0, i], PD6[0, j]], [PD6[1, i], PD6[1, j]], 'r-')
ax6.set_title('Zoom in 150%')


plt.show()


            