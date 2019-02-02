#!/usr/bin/python
print("Please input a number. This program will compute whether this number is prime.")
num = int(input())
divlist = []

for x in range(1, num+1):
	if num%x ==0:
		divlist.append(x)
#print(divlist)

if len(divlist) <= 2:
	print(str(num) + " is a prime number.")