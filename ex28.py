#!/usr/bin/python3
def findmax(num1, num2, num3):

	if num1 > num2 and num1 >num3:
		print("Num1 is largest")
	if num2 > num1 and num2 >num3:
		print("Num2 is largest")
	if num3 > num2 and num3 >num1:
		print("Num3 is largest")

findmax(6, 2, 10)