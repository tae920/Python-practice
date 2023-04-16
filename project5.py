# Author: Taeseok LEE (u3230402)
# Assignment 1 Part 5
# Date created: 18/7/2021

import turtle as w # w is the reference variable

w.speed(0)

# Repositioning the position of the pen for the output
w.penup()
w.goto(48, 115)
w.pendown()

# Changing colors
w.pencolor('red')
w.fillcolor('red')

# Filling the color of the figure
w.begin_fill()

# Drawing a figure
for i in range(6):
    w.right(60)
    w.forward(100)
w.end_fill()

# Repositioning the position of the pen for the output
w.penup()
w.goto(0, 0)
w.pendown()

# Displaying text
w.pencolor('white')
style = ('Times New Roman', 50, 'normal')
w.write('STOP', font=style, align='center')
w.hideturtle()
w.done()