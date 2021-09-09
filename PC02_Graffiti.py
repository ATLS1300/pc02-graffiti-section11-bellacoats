#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: BellaCoats
September 3, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.speed(9)

#Jeff left horn
turtle.pensize(4)
turtle.color(255,0,0)
turtle.begin_fill()

turtle.penup()
turtle.goto(-35,190)
turtle.pendown()
turtle.left(120)
turtle.forward(90)
turtle.left(150)
turtle.forward(105)
turtle.left(120)
turtle.forward(52)
turtle.end_fill()

#right horn
turtle.pensize(4)
turtle.color(255,0,0)
turtle.begin_fill()

turtle.penup()
turtle.goto(5,190)
turtle.pendown()
turtle.left(30)
turtle.forward(90)
turtle.right(150)
turtle.forward(95)
turtle.right(110)
turtle.forward(50)
turtle.end_fill()

#mustache
turtle.pensize(3)
turtle.color(255,0,0)


turtle.penup()
turtle.goto(15,67)
turtle.pendown()
turtle.left(30)
turtle.forward(20)
turtle.left(20)
turtle.forward(10)
turtle.left(150)
turtle.forward(60)
turtle.left(140)
turtle.forward(13)
turtle.left(40)
turtle.forward(20)

#devil fork
turtle.pensize(14)
turtle.color(255,0,0)

turtle.penup()
turtle.goto(-15,-250)
turtle.pendown()
turtle.right(115)
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
#actual fork parts
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(65)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(65)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(65)

#text bubble
turtle.penup()
turtle.goto(-175,125)
turtle.pendown()
turtle.begin_fill()
turtle.color("RoyalBlue")
turtle.circle(95)
turtle.right(110)
turtle.forward(75)
turtle.right(150)
turtle.forward(75)
turtle.end_fill()

turtle.penup()
turtle.goto(-340,175)
turtle.color("FloralWhite")
style = ('Arial', 22, 'bold')
turtle.write("NO YOU DON'T ", font = style)
turtle.goto(-335,150)
turtle.write("GET A BREAK ", font = style)
turtle.goto(-340,125)
turtle.write("TODAY IDIOT <3", font = style)



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
