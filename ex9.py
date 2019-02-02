#!/usr/bin/python
import random
print("Guess a number between 1 and 9")
guess = int(input())

num = random.randint(1,9)


while guess != num:
	if guess < num:
		print("Higher!")
	elif guess > num:
		print ("Lower!")
	print("Make a new guess!")
	guess = int(input())


print("You guessed right!")

