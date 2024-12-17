#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: November 20, 2024
#This program implements the pseudocode below:
# for i = 90, 88, 86, 84, 82, ... ,0:
# 	Walk forward 25 steps
# 	Turn left i degrees

import turtle

carey = turtle.Turtle() 


for i in range(90,0,-2):
    carey.forward(25)
    carey.left(i)


turtle.Screen().exitonclick()


