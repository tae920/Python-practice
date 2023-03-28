# A python program that reads data from file and calculate average with data
# Author : Taeseok LEE
# Assessment : Assignment 2 Project 2
# Date Created : 24/8/2021

# Setting the list
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
dayForMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
steps = []

# Read data from the file line by line
try:
    infile = open('steps.txt', 'r')
    line = infile.readline()
    while line != '':
        line = line.rstrip('\n')
        number = int(line)
        steps.append(number)
        line = infile.readline()
    infile.close()
except FileNotFoundError as f:
    print(f)

# Calculate average steps and print them
n = 0
m = dayForMonth[0]
print('The average number of steps taken for each month')
for i in range(12):
    average= sum(steps[n:m])/dayForMonth[i]
    print(f'''{months[i]} : {average:.4f}''')
    n =n + dayForMonth[i]
    m = m + dayForMonth[i+1]
