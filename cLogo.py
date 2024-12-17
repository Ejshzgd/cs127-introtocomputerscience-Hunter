#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: December 17, 2024
#This programs creates a 'C' logo for CUNY on a 30x30 grid.

import matplotlib.pyplot as plt 
import numpy as np 

img = np.zeros((30,30,3))
img[:10,:,2] = 1
img[20:,:,2] = 1
img[10:20,:10,2] = 1
img[10:20,10:,:] = 1

plt.imsave("logo.png", img)