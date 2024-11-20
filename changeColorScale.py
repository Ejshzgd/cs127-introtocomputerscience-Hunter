#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: November 20, 2024
#The programs modifys the region of the map with elevation greater than 6 feet and less than or equal 20 feet above sea level to the color grey


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        elif elevations[row,col] <= 20:
            #Above 6 feet, but less than or equal 20 feet
            floodMap[row,col,0] = 0.5    #Set the red channel to 50%
            floodMap[row,col,1] = 0.5    #Set the green channel to 50%
            floodMap[row,col,2] = 0.5    #Set the blue channel to 50%
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%


# for row in range(mapShape[0]):
#     for col in range(mapShape[1]):
#         if elevations[row,col] <= 20:
#             #Above 6 feet, but less than or equal 20 feet
#             floodMap[row,col,0] = 0.5    #Set the red channel to 50%
#             floodMap[row,col,1] = 0.5    #Set the green channel to 50%
#             floodMap[row,col,2] = 0.5    #Set the blue channel to 50%



# Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

# Display the plot:
plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)