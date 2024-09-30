#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 30, 2024
#This program draws a cornflower blue pentagon 

import turtle

carey = turtle.Turtle()
turtle.colormode(255)
carey.shape("turtle")
carey.color("cornflowerblue")

for i in range (5):
    carey.forward(100)
    carey.left(360/5)
    carey.stamp()

turtle.Screen().exitonclick()
