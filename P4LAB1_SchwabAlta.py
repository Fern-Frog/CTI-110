# Alta Schwab
# 10/29/2024
# P2LAB1
# Use loops and the turtle library to draw a house

# import turtle library
import turtle 

# Set up the window and turtle object
window = turtle.Screen()
timothy = turtle.Turtle()

# Change the features of turtle
timothy.pensize(18)
timothy.pencolor("DarkSeaGreen2")
timothy.shape("classic")

# while loop that runs 4 times
sq_sides = 0

while sq_sides <= 3:
    sq_sides += 1
    timothy.forward(100)
    timothy.right(90)

# For loop to run 3 time
for tri_sides in range(3):
    timothy.forward(100)    
    timothy.left(120)




