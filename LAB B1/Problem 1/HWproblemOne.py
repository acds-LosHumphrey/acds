#-------------------------------------------------------------------------------
# Name:        Problem 1
# Purpose:     HW
#
# Author:      okre1
#
# Created:     07/02/2018
# Copyright:   (c) okre1 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#INPUTS

print("Program that checks if two numbers are even or odd\n")
num = int(input("Enter one number (bigger than 1) to check: "))
check = int(input("Enter one number to divide by: "))

#TEST LOOPS

if num > 1:
    if (num%2) == 0:
        print(num,"is even.\n")
    else:
        print(num,"is odd\n")
    if (num%4) == 0:
        print(num,"is divisible by 4")
    else:
        print(num,"is not divisible by 4")

    if (num % check) == 0:
        print(check,"divides evenly into ", num)
    else:
        print(check,"doesn't divide evenly into ", num)

for cont in range(2,num):
    if (num % cont) == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")




