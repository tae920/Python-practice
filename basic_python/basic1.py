# Author: Taeseok LEE 
# Date created: 13/7/2021

# Collecting informations
employeeName = input("Enter employee's name: ")
workedHour = float(input('Enter number of hours worked in a week: '))
hourlyPayRate = float(input("Enter hourly pay rate: "))
atoRate = float(input("Enter ATO tax withholding rate: "))
medicareRate = float(input("Enter Medicare Levy rate: "))

# Fomulas to calculate
grossPay = workedHour * hourlyPayRate
atoTax = grossPay * atoRate
medicareLevy = grossPay * medicareRate
totalDeduction = atoTax + medicareLevy
netPay = grossPay - totalDeduction

# Printing the output
print(f'''
Employee Name: {employeeName}
Hours worked: {workedHour}
Pay Rate: ${hourlyPayRate}
Gross Pay: ${grossPay}
Deductions:
    ATO tax({atoRate*100}%): ${atoTax}
    Medicare Levy({medicareRate*100}%): ${medicareLevy}
    Total Deduction: ${totalDeduction}

Net Pay: ${netPay}''')