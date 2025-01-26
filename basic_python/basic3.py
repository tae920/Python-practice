# Author: Taeseok LEE
# Date created: 13/7/2021

import turtle as w  # w is the reference variable

# Getting information from the user
organismStarts = int(w.numinput('Organism', 'Enter starting number of organisms'))
increaseAvg = int(w.numinput('Average daily increase', 'Enter the average daily population \nincrease(as a percentage)'))
numOfDays = int(w.numinput('Number of days','Enter the number of days the organisms \nwill be left to multiply'))

# Setting font style
style1 = ('Times New Roman', 30, 'bold')
style2 = ('Times New Roman', 30, 'normal')

# Changing background color
w.bgcolor('sky blue')

# Repositioning the position of the pen for the output
w.penup()
w.goto(-240, 150)
w.pendown()

# Setting the size of the turtle's window
w.setup(600)

# Changing the angle
w.right(90)

# Displaying text
w.write("{0:<25s}{1:>10s}".format("Day Approximate", "Population"), font=style1)

# Repositioning the position of the pen so that the text does not overlap
w.penup()
w.forward(30)
w.pendown()

# Using for loop to repeat the same process
for x in range(numOfDays):
    dayApprox = x+1
    w.write("{0:<40}{1:<.5f}".format(dayApprox, organismStarts), font=style2)
    w.penup()
    w.forward(30)
    w.pendown()
    organismStarts +=(organismStarts * (increaseAvg/100))

# Hiding the cursor
w.hideturtle()
w.done()