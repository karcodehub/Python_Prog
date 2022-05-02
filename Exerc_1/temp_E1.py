# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# test if x is divisible by 2 and 3 or one of these numbers
x = 15
y = 15
z = 20

if x % 2 == 0:
 if x % 3 == 0:
  print('Divisible by 2 and 3')
 else:
  print('Divisible by 2 but not by 3')
elif x % 3 == 0:
 print('Divisible by 3 but not by 2')

x = 15
y = 15
z = 20

# # Determine the minimum of three numbers

if x < y and x < z:
 print(x, 'is the minimum!')
elif y < z: 
 print(y, 'is the minimum!')
else:
 print(z, 'is the minimum!')

    
# # Repeat a word: try only with If

word = input('Which word should I repeat? ')
number = int(input('How many times should I repeat the word? '))
to_print = ''
if number == 1:
 to_print = word
elif number == 2:
 to_print = word + word
elif number == 3:
 to_print = word + word + word
# #...
 print(to_print)


# repeat a word: with While loop

word = input('Which word should I repeat? ')
number = int(input('How many times should I repeat the word? '))
to_print = ''
zaehler = 0
while zaehler < number: 
 zaehler = zaehler + 1 
 print('In the loop:', zaehler)
 to_print = to_print + word 
print(to_print)


# find a positive integer that is divisible by both 11 and 12

x = 1
while True:
 if x%11 == 0 and x%12 == 0:
   break
 x = x + 1
print(x, 'is divisible by 11 and 12')


