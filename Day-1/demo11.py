'''
s = '123456789'
Given string str,
Write a python program to calculate sum of the digits.
use the for loop.
'''

str = '123456789'
total = 0

for char in str:
    total = total + int(char) #print(char,type(char))

print(f"Sum of the digits in string str is : {total}")