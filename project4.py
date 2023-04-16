# A python GUI program using list and listbox to calculate average of scores
# Author : Taeseok LEE
# Assessment : Assignment 2 Project 4
# Date Created : 28/8/2021

import tkinter
from tkinter import *
from tkinter import messagebox

# Function to input values to the listbox
def get_scores():
    listdays.insert(tkinter.END, conOfEntScore.get())
    entScore.delete(0, END)

# Function to calculate the average
def calculate():
    try:
        for i in range(10):
            scores.append(float(listdays.get(i)))
    except ValueError:
        messagebox.showerror('hi', 'You should input 10 scores')
    scores.sort()
    conOfEntTotal.set(sum(scores))
    conOfEntLowest.set(scores[0])
    result = (sum(scores) - scores[0])/9
    conOfEntResult.set(result)

def reset_list():
    listdays.delete(0,END)

scores = []

# Setting the window
window = Tk()
window.title("Student Grade Calculator")
window.geometry("250x435")

# Enter Scores
lblScore = Label(window, text = "Enter 10 test scores")
lblScore.grid(row = 0, column = 0, columnspan = 2)

conOfEntScore = StringVar()
entScore = Entry(window, width = 15, textvariable = conOfEntScore)
entScore.grid(row = 1, column = 0, columnspan = 2)

btnScore = Button(window, width = 15, text = "Enter", command = get_scores)
btnScore.grid(row=2, column = 0, columnspan = 2)

#Listbox
var2 = StringVar()
listdays = Listbox(window, height=10, width=15, listvariable=var2)
listdays.grid(row = 3, column = 0, columnspan = 2)

# Display the Total
lblTotal = Label(window, text = 'Total score')
lblTotal.grid(row = 5, column = 0)

conOfEntTotal = StringVar()
entTotal = Entry(window, width = 15,state ='readonly', textvariable = conOfEntTotal)
entTotal.grid(row = 5, column = 1)

# Display the Lowest score
lblLowest = Label(window, text = 'Lowest score')
lblLowest.grid(row = 6, column = 0)

conOfEntLowest = StringVar()
entLowest = Entry(window, width = 15,state ='readonly', textvariable = conOfEntLowest)
entLowest.grid(row = 6, column = 1)

# Display the average
lblLowest = Label(window, text = 'The Average')
lblLowest.grid(row = 7, column = 0)

conOfEntResult = StringVar()
entResult = Entry(window, width = 15,state ='readonly',textvariable = conOfEntResult)
entResult.grid(row = 7, column = 1)

# Calculate all results
btnCalculate = Button(window,height=2, width = 20, text = "Calculate", command = calculate)
btnCalculate.grid(row= 8, column = 0, columnspan = 2)

# Reset list
btnReset = Button(window, width = 15, text = "Reset Listbox", command = reset_list)
btnReset.grid(row=4, column = 0, columnspan = 2)

# Finish the program
btnExit = Button(window,height=2, width = 20, text = "Exit", command = window.destroy)
btnExit.grid(row= 9, column = 0, columnspan = 2)

window.mainloop()