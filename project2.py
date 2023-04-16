# Author: Taeseok LEE (u3230402)
# Assignment 1 Part 2
# Date created: 17/7/2021

# Restaurant names
num1 = "Joe's Gourmet Burgers"
num2 = "Main Street Pizza Company"
num3 = "Corner Café"
num4 = "Mama's Fine Italian"
num5 = "The Chef's Kitchen"

# Function to get answers from the user
def customerAnswer():
    vegeAnswer = input('Is anyone in your party a vegetarian?(Enter YES or NO): ')
    veganAnswer = input('Is anyone in your party a vegan?(Enter YES or NO): ')
    glutenAnswer = input('Is anyone in your party gluten-free?(Enter YES or NO): ')
    vegeAnswer = vegeAnswer.upper()
    veganAnswer = veganAnswer.upper()
    glutenAnswer = glutenAnswer.upper()
    return vegeAnswer, veganAnswer, glutenAnswer

# Function to evaluate restaurants that user can go
def analyseAnswer(vegeAnswer, veganAnswer, glutenAnswer):
    if vegeAnswer == "YES":
        if veganAnswer == "YES":
            chosenResults = num3 + '\n' + num5
        elif veganAnswer == "NO":
            if glutenAnswer == "YES":
                chosenResults = num2 + '\n' + num3 + '\n' + num5
            elif glutenAnswer == "NO":
                chosenResults = num2 + '\n' + num3 + '\n' + num4 + '\n' + num5
    elif vegeAnswer == "NO":
        if veganAnswer == "YES":
            chosenResults = num3 + '\n' + num5
        if veganAnswer == "NO":
            if glutenAnswer == "YES":
                chosenResults = num2 + '\n' + num3 + '\n' + num5
            elif glutenAnswer == "NO":
                chosenResults = num1 + '\n' + num2 + '\n' + num3 + '\n' + num4 + '\n' + num5
    return chosenResults

# Function to print the result
def displayResult(restaurant):
    print('Here are your restaurant choices:\n' + restaurant)

# The main Function
def main():
    vegetarian, vegan, gluten = customerAnswer()
    chosenResults = analyseAnswer(vegetarian, vegan, gluten)
    displayResult(chosenResults)

main()