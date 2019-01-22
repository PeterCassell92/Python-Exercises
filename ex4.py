#!/usr/bin/python
print("Please input a number. This program will find all of the divisors of that number")
num = input()
divlist = []

for x in range (1, num+1):
	if num%x ==0:
		divlist.append(x)
print(divlist)

