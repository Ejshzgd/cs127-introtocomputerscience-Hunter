#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 25, 2024
#This program displays different shades of a color

import turtle
carey = turtle.Turtle()
turtle.colormode(255)
carey.backward(100)

for i in range(0, 260, 10):
    carey.forward(10)
    carey.pensize(i)
    carey.color(0,0,i)

turtle.Screen().exitonclick()