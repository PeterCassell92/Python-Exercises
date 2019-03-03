#!/usr/bin/python3
import random

def printwordwithgaps(word):
	displayword = " ".join(word)
	print(displayword)
	pass

def chooserandomfromlist(mylist):
	secure_random = random.SystemRandom() #not needed but this is how to do cryptographically secure random.
	return str((secure_random.choice(wordlist)))

def setupnewgame(mylist):
	newword = chooserandomfromlist(mylist)
	resetguessword =len(newword)*('_')
	printwordwithgaps(resetguessword)
	return newword, resetguessword, [''], 6

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def loaddictionary():
	textfile = selectdifficulty()
	with open(textfile, 'r') as open_file:
		line = open_file.readline()
		dictlist = []
		while line:
			dictlist.append(line.strip().upper())
			line = open_file.readline()
		return dictlist

def selectdifficulty():
	print("Press 1 for easy mode or 2 for hard mode.")
	selection = int(input())
	if selection == 1:
		textfile = "hangmaneasy.txt"
		return textfile
	elif selection == 2:
		textfile = "sowpods.txt"
		return textfile


wordlist = loaddictionary()
word , guessword, guesslist, guessesleft = setupnewgame(wordlist)


while guessword != word:
	print("Please enter new guess")
	charguess = str(input()).upper()
	if len(charguess) != 1:
		continue
	if charguess not in guesslist:
		guesslist.append(charguess)
		
	elif charguess in guesslist:
		print("You have already guessed this character. Please guess again")
		continue
	hit = False
	for a in range (0, len(word)):
		if word[a] == charguess:
			guessword = guessword[0:a]+ charguess + guessword[a+1:]
			hit = True
	if not hit:
		guessesleft -= 1

	printwordwithgaps(guessword)
	print("You have " + str(guessesleft) + " incorrect guesses remaining.")
	print(str(guesslist[1:]))

	if guessesleft == 0:
		print("You Lose. The hidden word was " + word)
		if yes_or_no("Would you like to play again?") == True:
			word , guessword, guesslist, guessesleft = setupnewgame(wordlist)


	elif guessword == word:
		print("Congratulations! You guessed the hidden word with " + str(guessesleft) + " trys left.")
		if yes_or_no("Would you like to play again?") == True:
			word , guessword, guesslist, guessesleft = setupnewgame(wordlist)

