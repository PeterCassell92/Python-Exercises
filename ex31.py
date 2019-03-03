#!/usr/bin/python3
import random

def printwordwithgaps(word):
	displayword = " ".join(word)
	print(displayword)
	pass


with open('sowpods.txt', 'r') as open_file:
	line = open_file.readline()
	wordlist = []
	while line:
		wordlist.append(line.strip())
		line = open_file.readline()

secure_random = random.SystemRandom() #not needed but this is how to do cryptographically secure random.
word = str((secure_random.choice(wordlist)))

guessword =len(word)*('_')

printwordwithgaps(guessword)


guesslist = [' ']
guessnum = 0
while guessword != word:
	print("Please enter new guess")
	charguess = str(input()).upper()
	if len(charguess) != 1:
		continue
	if charguess not in guesslist:
		guesslist.append(charguess)
		guessnum += 1
	else:
		print("You have already guessed this character. Please guess again")
	
	for a in range (0, len(word)):
		if word[a] == charguess:
			guessword = guessword[0:a]+ charguess + guessword[a+1:]
		

	printwordwithgaps(guessword)
	print("You have had " + str(guessnum) + " guesses so far.")
	print(str(guesslist[1:]))

print("Congratulations! You guessed the hidden word in " + str(guessnum) + " attempts.")		




