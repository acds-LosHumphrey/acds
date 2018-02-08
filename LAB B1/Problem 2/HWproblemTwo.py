#-------------------------------------------------------------------------------
# Name:        Problem 2
# Purpose:
#
# Author:      okre1
#
# Created:     08/02/2018
# Copyright:   (c) okre1 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
#SET LISTS

a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#COMPARE LISTS AND DISPLAY SAME ELEMENTS

c = set(a) & set(b)
print(c)

#RANDOM SUFFLE OF LISTS 'a' & 'b' AND COMPARE ELEMENTS

random.shuffle(a)
random.shuffle(b)

c = set(a) & set(b)
print("Scrambled list 'a':", a, "\nScrambled list 'b':",b,"\nMutual Elem:",c)



