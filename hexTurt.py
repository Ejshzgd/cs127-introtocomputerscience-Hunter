#Name: Carey Jiang
#Email: carey.jiang65@myhunter.cuny.edu
#Date: September 25, 2024
#This program prompts the user for a hex code and then displays it

import turtle

carey = turtle.Turtle()
carey.shape("turtle")

favColor = input("Enter a hex string:  ")

carey.color(favColor)

turtle.Screen().exitonclick()

