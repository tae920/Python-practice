# A python program using classes and objects to manage employees
# Author : Taeseok LEE
# Date Created : 30/8/2021

# Importing classes
from employee_management_system.employee_class import Employee
from employee_management_system.employee_subclass1 import ShiftEmployee
from employee_management_system.employee_subclass2 import Contractor
import pickle
import os.path

# Main Function
def main():
    employeeInfo = check_file()
    menu(employeeInfo)

# Function to check file existence(opens file if it exists, save file from object if it doesn't exist)
def check_file():
    if os.path.isfile('employeelist.p'):
        with open('employeelist.p', 'rb') as file:
            empList = pickle.load(file)
    else:
        empList = get_file()
    return empList

# Function to get data from object and put it into a dictionary and save it to the file
def get_file():
    first, second, third = store_object()
    empList = {first.get_id(): [first.get_name(),first.get_department(),first.get_job_title()]
                ,second.get_id(): [second.get_name(),second.get_department(),second.get_job_title()]
                ,third.get_id(): [third.get_name(),third.get_department(),third.get_job_title()]}
    with open('employeelist.p', 'wb') as file:
        pickle.dump(empList, file)

    with open('employeelist.p', 'rb') as file:
        empList = pickle.load(file)
    return empList

# Function that includes object with employee data in it
def store_object():
    firstEmployee = Employee('Susanna Myer', 47899, 'Accounting', 'Vice President')
    secondEmployee = Employee('Mark Joseph', 39119, 'Info Tech', 'Programmer')
    thirdEmployee = Employee('Joyce Roberts', 81774, 'Manufacturing', 'Engineer')
    return firstEmployee, secondEmployee, thirdEmployee

# Function to choose menu
def menu(employeeInfo):
    print(f'''    
    Menu
    a. Look up an employee
    b. Add a new employee
    c. Change employee date
    d. Delete an employee
    e. Shift Employee
    f. Contractor
    g. Quit
    ''')
    chosenMenu = input('Enter an alphabet: ')
    if chosenMenu == 'a':
        lookup_employee(employeeInfo)
    elif chosenMenu == 'b':
        add_new_emp(employeeInfo)
    elif chosenMenu == 'c':
        change_employee(employeeInfo)
    elif chosenMenu == 'd':
        delete_Employee(employeeInfo)
    elif chosenMenu == 'e':
        shift_employee(employeeInfo)
    elif chosenMenu == 'f':
        contractor(employeeInfo)
    elif chosenMenu == 'g':
        with open('employeelist.p', 'wb') as file:
            pickle.dump(employeeInfo, file)
        exit()
    else:
        print('You should choose a alphabet between a ~ g\nGoing back to menu')
        menu(employeeInfo)

# Function to look up information of employee
def lookup_employee(employeeInfo):
    try:
        search = int(input("Enter the employee ID: "))
    except ValueError:
        print('\nID should be numbers\n')
        lookup_employee(employeeInfo)
    if search not in employeeInfo:
        print('\n',search, "does not exist\nPlease check the ID again\n")
        menu(employeeInfo)
    else:
        print(f'''
        Name: {employeeInfo[search][0]}
        Department: {employeeInfo[search][1]} 
        Job Title: {employeeInfo[search][2]}''')
    menu(employeeInfo)

# Function to add new employee
def add_new_emp(employeeInfo):
    try:
        newId = int(input("Enter the ID number: "))
    except ValueError:
        print('\nID should be numbers\n')
        add_new_emp(employeeInfo)
    if newId not in employeeInfo:
        newName = input("Enter employee name: ")
        newDepart = input("Enter Department: ")
        newJobTitle = input("Enter Job title: ")
        addEmployee =[newName, newDepart, newJobTitle]
        employeeInfo[newId]  = addEmployee
        print(newId, "has been added")
    else:
        print(newId, "already exists")
    menu(employeeInfo)

# Function to change employee details from existing employee
def change_employee(employeeInfo):
    try:
        theId = int(input("Enter the ID number: "))
    except ValueError:
        print('\nID should be numbers\n')
        change_employee(employeeInfo)
    if theId in employeeInfo:
        theName = input("Enter employee name: ")
        theDepart = input("Enter Department: ")
        theJobTitle = input("Enter Job title: ")
        updateEmployee =[theName, theDepart, theJobTitle]
        employeeInfo[theId]  = updateEmployee
        print(theId, "has been updated")
    else:
        print(theId, "does not exist")
    menu(employeeInfo)

# Function to delete existing employee
def delete_Employee(employeeInfo):
    try:
        delId = int(input("Enter the ID number: "))
    except ValueError:
        print('\nID should be numbers\n')
        delete_Employee(employeeInfo)
    if delId in employeeInfo:
        del employeeInfo[delId]
        print(delId, "has been deleted successfully")
    else:
        print(delId, "does not exist")
    menu(employeeInfo)

# Function to input information of Shift employee and print them
def shift_employee(employeeInfo):
    try:
        firstID = int(input('\nFirst Shift Employee\nEnter the ID: '))
    except ValueError:
        print('\nID should be numbers\n')
        shift_employee(employeeInfo)
    firstName = input('Enter the name: ')
    firstDepart = input('Enter the Department: ')
    firstJobTitle = input('Enter the Job Title: ')
    firstShiftNum = int(input('Enter the Shift Number: '))
    if firstShiftNum == 1:
        pass
    elif firstShiftNum == 2:
        pass
    else:
        print('Shift Number should be 1 or 2')
        shift_employee(employeeInfo)
    firstPayRate = input('Enter the Hourly Pay Rate: ')
    firstShiftEmployee = ShiftEmployee(firstName,firstID,firstDepart,firstJobTitle,
                                       firstShiftNum,firstPayRate)

    try:
        secondID = int(input('\nSecond Shift Employee\nEnter the ID: '))
    except ValueError:
        print('\nID should be numbers\n')
        shift_employee()
    secondName = input('Enter the name: ')
    secondDepart = input('Enter the Department: ')
    secondJobTitle = input('Enter the Job Title: ')
    secondShiftNum = int(input('Enter the Shift Number: '))
    if secondShiftNum == 1:
        pass
    elif secondShiftNum == 2:
        pass
    else:
        print('Shift Number should be 1 or 2')
        shift_employee(employeeInfo)
    secondPayRate = input('Enter the Hourly Pay Rate: ')
    secondShiftEmployee = ShiftEmployee(secondName, secondID, secondDepart, secondJobTitle,
                                        secondShiftNum, secondPayRate)
    print(f'''
    First Shift Employee
    ID : {firstShiftEmployee.get_id()}
    Name : {firstShiftEmployee.get_name()}
    Department : {firstShiftEmployee.get_department()}
    Job Title : {firstShiftEmployee.get_job_title()}
    Shift Number : {firstShiftEmployee.get_shift_num()}
    Hourly Pay Rate : {firstShiftEmployee.get_pay_rate()}

    Second Shift Employee
    ID : {secondShiftEmployee.get_id()}
    Name : {secondShiftEmployee.get_name()}
    Department : {secondShiftEmployee.get_department()}
    Job Title : {secondShiftEmployee.get_job_title()}
    Shift Number : {secondShiftEmployee.get_shift_num()}
    Hourly Pay Rate : {secondShiftEmployee.get_pay_rate()}
    
    Going back to menu''')
    menu(employeeInfo)

# Function to input information of Contractor and print them
def contractor(employeeInfo):
    try:
        firstID = int(input('\nFirst Contractor\nEnter the ID: '))
    except ValueError:
        print('\nID should be numbers\n')
        contractor(employeeInfo)
    firstName = input('Enter the name: ')
    firstDepart = input('Enter the Department: ')
    firstJobTitle = input('Enter the Job Title: ')
    firstEndDate = input('Enter Contract End Date: ')
    firstABN = input('Enter ABN: ')
    firstSalary = input('Enter Fixed Contract Salary: ')
    firstContractor = Contractor(firstName,firstID,firstDepart,firstJobTitle,firstEndDate,
                                 firstABN,firstSalary)

    try:
        secondID = int(input('\nSecond Contractor\nEnter the ID: '))
    except ValueError:
        print('\nID should be numbers\n')
        contractor(employeeInfo)
    secondName = input('Enter the name: ')
    secondDepart = input('Enter the Department: ')
    secondJobTitle = input('Enter the Job Title: ')
    secondEndDate = input('Enter Contract End Date: ')
    secondABN = input('Enter ABN: ')
    secondSalary = input('Enter Fixed Contract Salary: ')
    secondContractor = Contractor(secondName, secondID, secondDepart, secondJobTitle,
                                  secondEndDate, secondABN, secondSalary)

    print(f'''
    First Contractor
    ID : {firstContractor.get_id()}
    Name : {firstContractor.get_name()}
    Department : {firstContractor.get_department()}
    Job Title : {firstContractor.get_job_title()}
    Contract End Date : {firstContractor.get_end_date()}
    ABN : {firstContractor.get_abn()}
    Salary : {firstContractor.get_salary()}

    Second Contractor
    ID : {secondContractor.get_id()}
    Name : {secondContractor.get_name()}
    Department : {secondContractor.get_department()}
    Job Title : {secondContractor.get_job_title()}
    Contract End Date : {secondContractor.get_end_date()}
    ABN : {secondContractor.get_abn()}
    Salary : {secondContractor.get_salary()}
    
    Going back to menu''')
    menu(employeeInfo)

main()
