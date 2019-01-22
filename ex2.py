#!/usr/bin/python
print("Please enter an integer. This program will determine whether that number is odd or even")
num = input()

remainder = num%2
if remainder == 0:
	print("The inputted number is even")
else:
	print("The inputted number is odd")

