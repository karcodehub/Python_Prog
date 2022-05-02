# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:22:12 2022

@author: Philipp Wolters
"""

# Task 1 (If statement)
# Read in the three numbers (or write numbers directly into the code, is also ok.)
print("Please enter 3 numbers one after the other.")
x = (int)(input("First number: "))
y = (int)(input("Second number: "))
z = (int)(input("Third number: "))

# Check if all numbers are even.
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print(min(x, y, z))
    
# Check if all numbers are odd.
if x%2 != 0 and y%2 != 0 and z%2 != 0:
    print(max(x, y, z))
    
# Check if exactly x and y are odd.
if x%2 != 0 and y%2 != 0 and z%2 == 0:
    print(max(x, y))

# Check if exactly x and z are odd.
if x%2 != 0 and y%2 == 0 and z%2 != 0:
    print(max(x, z))

# Check if exactly y and z are odd.
if x%2 == 0 and y%2 != 0 and z%2 != 0:
    print(max(y, z))

# Check if only x is odd.
if x%2 != 0 and y%2 == 0 and z%2 == 0:
    print(x)
    
# Check if only y is odd.
if x%2 == 0 and y%2 != 0 and z%2 == 0:
    print(y)
    
# Check if only z is odd.
if x%2 == 0 and y%2 == 0 and z%2 != 0:
    print(z)
    