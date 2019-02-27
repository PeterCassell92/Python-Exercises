#!/usr/bin/python3
#This program draws a psuedo-graphics gamebox of X by X squares where X is a positive integer.
		
def drawgamebox(gridsize):
	if gridsize !=0:	
		for x in range (0, gridsize-1):
			print((gridsize-1)*(" ---") + " --- ")
			print((gridsize-1)*("|   ") + "|   |")

		print((gridsize-1)*(" ---") + " --- ")
		print((gridsize-1)*("|   ") + "|   |")
		print((gridsize-1)*(" ---") + " --- ")


drawgamebox(5)