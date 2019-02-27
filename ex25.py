#!/usr/bin/python3

def findintegermidpoint(num1, num2):
	if num1 > num2:
		larger = num1
		smaller = num2
	elif num1 < num2:
		larger = num2
		smaller = num1
	elif num1 == num2:
		return num1

	difference = larger - smaller
	mid = int(difference/2) +smaller
	return mid


if __

print("Pick a number between 0 and 100. \n The program will try to guess that number in as few attempts as possible.")
num = int(input())

upperbound = 100
lowerbound = 0
midpoint = findintegermidpoint(upperbound, lowerbound)
guess = midpoint
print("Computer's initial guess is "+str(midpoint))
attempts = 1

while guess != num:
	
	if guess < num:
		lowerbound = guess
	elif guess > num:
		upperbound = guess
	guess = findintegermidpoint(lowerbound,upperbound)
	print(guess)
	attempts += 1

print("The computer has guessed " +str(guess) + " after " + str(attempts) + " attempts")
