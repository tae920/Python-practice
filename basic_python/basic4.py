# Author: Taeseok LEE
# Date created: 18/7/2021

# Function to check validity of the password
def check_password(num):
    digit = 0
    alpha = 0
    val = True
    for d in num:
        if d.isdigit():
            digit += 1
    for c in num:
        if c.isalpha():
            alpha += 1
    if (len(num) < 8):
        val = False
    if not num.isalnum():
        val = False
    if digit < 2:
        val = False
    if alpha < 1:
        val = False
    return val

# Function to print result
def print_result(result):
    if result == False:
        print('Invalid Password')
    else:
        print('Valid Password')

# The main Function
def main():
    password = input('Enter a string for password: ')
    validity = check_password(password)
    print_result(validity)

main()