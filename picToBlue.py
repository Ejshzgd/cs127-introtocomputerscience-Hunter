#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: November 13, 2024
#This program takes an image, loads and displays it, and then saves a new image with only the blue channel

import matplotlib.pyplot as plt
import numpy as np

inFile = input("Enter name of the input file:  ")    #Takes an image
outFile = input("Enter name of the output file:  ")  #Outputs the saved image

inFile = 'csBridge.png'      #csBridge.png

img = plt.imread(inFile)      #Takes an .png image
# plt.imshow(img)                      #Loads the image into plt
# plt.show()                           #Shows the image to the screen

img[:,:,0] = 0                      #Set the red channel to 0
img[:,:,1] = 0                      #Set the green channel to 0


imgNext = plt.imread('acTree.png')
imgNext[:,:,0] = 0                      #Set the red channel to 0
imgNext[:,:,1] = 0                      #Set the green channel to 0


# plt.imshow(imgNext)                     #Loads the image into plt
# plt.show()                           #Shows the image to the screen

plt.imsave('out1.png', img)        #Saves img2 as "blueCsBridge"
plt.imsave('out2.png', imgNext)