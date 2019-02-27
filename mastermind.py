#! /usr/bin/python
import random
Mastermind = str(random.randint(10000,99999))

#print Mastermind[0]
print("Welcome to Mastermind.\r\n\r\nThe computer is thinking of a number between 10000 and 99999.\r\nYou must decipher what this number is within 5 guesses.\r\nA * means you've exactly matched that number in that position.\r\nA ^ means that the number is correct but in the incorrect position.\r\n\r\n")

for x in range (5):
	b=0
	match=[0,0,0,0,0]
	Guess= str((input("Enter your 5 digit integer for guess number %s: " % (x+1))))
	for y in range (5):
		for z in range (5):
			if Guess[y] == Mastermind[z] : #or Guess[y] == Mastermind[1] or Guess[y] == Mastermind[2] or Guess[y]== Mastermind[3] or Guess[y] == Mastermind[4] : 
				if match[y] != "*"	:
					if Guess[y] == Mastermind[y] :
						match[y]= "*"
						b=b+1
					else :
						match[y]= "^"
					if b==5 :
						print("You are a mastermind!! Well done!")
	print(str(match) + "\r\n")

print("The correct answer was %s" % Mastermind)