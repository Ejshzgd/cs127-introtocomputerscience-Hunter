#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 30, 2024
#This program turns a turtle based on user input and then moves forward 100
import turtle

carey = turtle.Turtle()

for i in range (5):
    deGre = int(input("Enter a number: "))
    carey.left(deGre)
    carey.forward(100)

turtle.Screen().exitonclick()
